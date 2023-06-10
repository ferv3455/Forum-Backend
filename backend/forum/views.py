import datetime
import traceback
from collections import Counter
from uuid import UUID
from zoneinfo import ZoneInfo

from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import AnonymousUser

from account.models import FollowList, FavoriteList
from core.query import query
from .models import Tag, Image, Post, Like, Comment
from .serializers import ImageSerializer, ImageFullSerializer, PostSerializer, PostFullSerializer, CommentSerializer, \
    LikeSerializer
from core.image import compress


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response({'message': 'hello!'}, status=status.HTTP_200_OK)


class PostListView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        # Get all posts according to filtering conditions
        # TODO: paging
        # Anonymous users can only get the full list
        if isinstance(request.user, AnonymousUser):
            if len(request.GET) != 0:
                return Response({'detail': 'Authentication credentials were not provided.'},
                                status=status.HTTP_401_UNAUTHORIZED)

        try:
            query_results = Post.objects

            # Filtering
            if 'user' in request.GET:
                query_results = query_results.filter(user__username=request.GET.get('user'))

            if 'filter' in request.GET:
                filter_name = request.GET.get('filter', 'null')
                if filter_name == 'hot':
                    # Get comments in the past day
                    comments = Comment.objects.filter(
                        createdAt__gt=datetime.datetime.now(tz=ZoneInfo('Asia/Shanghai')) - datetime.timedelta(1))
                    posts = comments.values_list('post', flat=True).all()
                    comment_count = Counter(posts)
                    postIds = [postId for postId, _ in comment_count.most_common(10)]
                    query_results = query_results.filter(id__in=postIds)
                elif filter_name == 'following':
                    follow_list = FollowList.objects.get(user=request.user)
                    query_results = query_results.filter(user__in=follow_list.following.all())

            if 'query' in request.GET:
                query_results = query(query_results, request.GET.get('query'))

            # Sorting
            sort_by = request.GET.get('sortBy', 'time')
            if sort_by == 'comments':
                query_results = query_results.order_by('-comments')
            elif sort_by == 'likes':
                query_results = query_results.order_by('-likes')
            elif sort_by == 'comment-time':
                query_results = query_results.order_by('-lastCommented')
            else:
                query_results = query_results.order_by('-createdAt')

            # Add isStarred data
            fav_list = FavoriteList.objects.get(user=request.user).favorites.values_list('id', flat=True)
            like_list = Like.objects.filter(user=request.user).values_list('post', flat=True)
            result = PostSerializer(query_results, many=True).data
            for value in result:
                value['isStarred'] = UUID(value['id']) in fav_list
                value['isLiked'] = UUID(value['id']) in like_list

            return Response(result, status=status.HTTP_200_OK)
        except Exception as exc:
            traceback.print_exc()
            return Response({'detail': repr(exc)}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        # Add a new post
        data = request.data
        try:
            new_post = Post.objects.create(title=data['title'], content=data['content'],
                                           user=request.user, location=data.get('location', None))
            new_post.images.add(*data['images'])

            for tag in data['tags']:
                if tag:
                    query = Tag.objects.filter(name=tag)
                    if len(query) == 0:
                        Tag.objects.create(name=tag)

            new_post.tags.add(*(tag for tag in data['tags'] if tag))
            return Response({'message': 'ok'}, status=status.HTTP_200_OK)
        except Exception as exc:
            traceback.print_exc()
            return Response({'detail': repr(exc)}, status=status.HTTP_400_BAD_REQUEST)


class PostDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        # Get detailed post
        query_result = Post.objects.get(id=id)
        fav_list = FavoriteList.objects.get(user=request.user).favorites.values_list('id', flat=True)
        like_list = Like.objects.filter(user=request.user).values_list('post', flat=True)
        result = PostFullSerializer(query_result).data
        result['isStarred'] = UUID(result['id']) in fav_list
        result['isLiked'] = UUID(result['id']) in like_list
        return Response(result, status=status.HTTP_200_OK)


class ImageView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        # Add a new image
        data = request.data
        try:
            img_base64 = data['data']
            compressed_base64 = compress(img_base64)
            new_image = Image.objects.create(content=img_base64, thumbnail=compressed_base64)
            return Response(ImageSerializer(new_image).data,
                            status=status.HTTP_200_OK)
        except Exception as exc:
            traceback.print_exc()
            return Response({'detail': repr(exc)}, status=status.HTTP_400_BAD_REQUEST)


class ImageInstanceView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        # Get the content of a certain image
        try:
            image = Image.objects.get(id=id)
            return Response(ImageFullSerializer(image).data,
                            status=status.HTTP_200_OK)
        except Exception as exc:
            traceback.print_exc()
            return Response({'detail': repr(exc)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        # Delete an image on the server
        try:
            Image.objects.get(id=id).delete()
            return Response({'message': 'ok'}, status=status.HTTP_200_OK)
        except Exception as exc:
            traceback.print_exc()
            return Response({'detail': repr(exc)}, status=status.HTTP_400_BAD_REQUEST)


class LikeView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, id, format=None):
        # Like a post
        try:
            user = request.user
            query = Like.objects.filter(user=user, post__id=id)
            if len(query) != 0:
                return Response({'detail': 'Already liked by the user'}, status=status.HTTP_400_BAD_REQUEST)

            post = Post.objects.get(id=id)
            Like.objects.create(user=user, post=post)
            return Response({'message': 'ok'}, status=status.HTTP_200_OK)
        except Exception as exc:
            traceback.print_exc()
            return Response({'detail': repr(exc)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        # Un-like a post
        try:
            user = request.user
            query = Like.objects.filter(user=user, post__id=id)
            if len(query) == 0:
                return Response({'detail': 'Not liked by the user yet'}, status=status.HTTP_400_BAD_REQUEST)

            query.delete()
            return Response({'message': 'ok'}, status=status.HTTP_200_OK)
        except Exception as exc:
            traceback.print_exc()
            return Response({'detail': repr(exc)}, status=status.HTTP_400_BAD_REQUEST)


class CommentView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        # Display all comments in a post
        # TODO: order
        try:
            post = Post.objects.get(id=id)
            query_results = Comment.objects.filter(post=post)

            # Sorting
            # time: the time of publication
            # hot: the number of likes (at least 3)

            sort_by = request.GET.get('sortBy', 'time')
            if sort_by == 'hot':
                query_results = query_results.filter(likes__gte=3).order_by('-likes')
            else:
                query_results = query_results.order_by('-createdAt')

            return Response(CommentSerializer(query_results, many=True).data,
                            status=status.HTTP_200_OK)

        except Exception as exc:
            traceback.print_exc()
            return Response({'detail': repr(exc)}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, id, format=None):
        # Comment a post
        try:
            user = request.user
            content = request.data['content']
            post = Post.objects.get(id=id)
            comment = Comment.objects.create(user=user, post=post, content=content)
            return Response({'message': 'ok'}, status=status.HTTP_200_OK)
        except Exception as exc:
            traceback.print_exc()
            return Response({'detail': repr(exc)}, status=status.HTTP_400_BAD_REQUEST)


class CommentLikeView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, id, format=None):
        # Like a comment
        try:
            comment = Comment.objects.get(id=id)
            comment.likes += 1
            comment.save()
            return Response({'message': 'ok'}, status=status.HTTP_200_OK)
        except Exception as exc:
            traceback.print_exc()
            return Response({'detail': repr(exc)}, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, id, format=None):
    #     # Un-like a comment
    #     try:
    #         comment = Comment.objects.get(id=id)
    #         comment.likes -= 1
    #         comment.save()
    #         return Response({'message': 'ok'}, status=status.HTTP_200_OK)
    #     except Exception as exc:
    #         traceback.print_exc()
    #         return Response({'detail': repr(exc)}, status=status.HTTP_400_BAD_REQUEST)


class LikeListView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        # Get all likes
        try:
            user = request.user
            query = Like.objects.filter(post__user=user)
            return Response(LikeSerializer(query, many=True).data, status=status.HTTP_200_OK)
        except Exception as exc:
            traceback.print_exc()
            return Response({'detail': repr(exc)}, status=status.HTTP_400_BAD_REQUEST)


class CommentListView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        # Get all comments
        try:
            user = request.user
            query = Comment.objects.filter(post__user=user)
            return Response(CommentSerializer(query, many=True).data, status=status.HTTP_200_OK)
        except Exception as exc:
            traceback.print_exc()
            return Response({'detail': repr(exc)}, status=status.HTTP_400_BAD_REQUEST)
