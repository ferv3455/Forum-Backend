from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post
from .serializers import PostSerializer, PostFullSerializer


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response({'message': 'hello!'}, status=status.HTTP_200_OK)


class PostListView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        # Get all posts
        sort_by = request.GET.get('sortBy', 'time')
        if sort_by == 'hot':
            query_results = Post.objects.all().order_by('-comments')
        elif sort_by == 'following':
            query_results = Post.objects.all().order_by('-likes')
        else:
            query_results = Post.objects.all().order_by('-createdAt')

        return Response(PostSerializer(query_results, many=True).data,
                        status=status.HTTP_200_OK)

    def post(self, request, format=None):
        # Add a new post
        data = request.data
        try:
            new_post = Post.objects.create(title=data['title'], content=data['content'], user=request.user)
            new_post.images.add(*data['images'])
            new_post.tags.add(*data['tags'])
            return Response({'message': 'ok'}, status=status.HTTP_200_OK)
        except Exception as exc:
            return Response({'detail': repr(exc)}, status=status.HTTP_400_BAD_REQUEST)


class PostDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        # Get detailed post
        query_result = Post.objects.get(id=id)
        return Response(PostFullSerializer(query_result).data,
                        status=status.HTTP_200_OK)
