from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from forum.models import Post
from .models import Profile, FollowList, FavoriteList
from .serializers import ProfileSerializer, FollowListSerializer, FavoriteListSerializer


# Create your views here.
def get_user(request, username=None):
    if username:
        user = User.objects.get(username=username)
    else:
        user = request.user
    return user


class ProfileView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, username=None, format=None):
        # Get personal profile of a user
        try:
            user = get_user(request, username)
            profile = Profile.objects.get(user=user)
            return Response(ProfileSerializer(profile).data,
                            status=status.HTTP_200_OK)
        except Exception as exc:
            return Response({'detail': repr(exc)}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, username=None, format=None):
        # Change avatar/description in the profile
        try:
            assert username is None, "Trying to edit another user's profile"
            data = request.data
            user = request.user
            profile = Profile.objects.get(user=user)

            if "description" in data:
                profile.description = data["description"]
            if "avatar" in data:
                profile.avatar = data["avatar"]

            profile.save()
            return Response({'message': 'ok'}, status=status.HTTP_200_OK)
        except Exception as exc:
            return Response({'detail': repr(exc)}, status=status.HTTP_400_BAD_REQUEST)


class UsernameView(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request, format=None):
        # Change username
        try:
            data = request.data
            user = request.user
            user.username = data["username"]
            user.save()
            return Response({'message': 'ok'}, status=status.HTTP_200_OK)
        except Exception as exc:
            return Response({'detail': repr(exc)}, status=status.HTTP_400_BAD_REQUEST)


class PasswordView(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request, format=None):
        # Change password
        try:
            data = request.data
            user = request.user
            assert user.check_password(data["old_password"]), "Old password invalid"
            user.set_password(data["password"])
            user.save()
            return Response({'message': 'ok'}, status=status.HTTP_200_OK)
        except Exception as exc:
            return Response({'detail': repr(exc)}, status=status.HTTP_400_BAD_REQUEST)


class FollowListView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, username=None, format=None):
        # Get follow list of a user
        try:
            user = get_user(request, username)
            follow_list = FollowList.objects.get(user=user)
            return Response(FollowListSerializer(follow_list).data,
                            status=status.HTTP_200_OK)
        except Exception as exc:
            return Response({'detail': repr(exc)}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, username=None, format=None):
        # Add follower
        try:
            assert username is None, "Trying to edit another user's following list"
            data = request.data
            users_to_follow = User.objects.filter(username__in=data["username"])
            user = request.user
            follow_list = FollowList.objects.get(user=user)
            follow_list.following.add(*users_to_follow)
            follow_list.save()
            return Response({'message': 'ok'}, status=status.HTTP_200_OK)
        except Exception as exc:
            return Response({'detail': repr(exc)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, username=None, format=None):
        # Remove follower
        try:
            assert username is None, "Trying to edit another user's following list"
            data = request.data
            users_to_unfollow = User.objects.filter(username__in=data["username"])
            user = request.user
            follow_list = FollowList.objects.get(user=user)
            follow_list.following.remove(*users_to_unfollow)
            follow_list.save()
            return Response({'message': 'ok'}, status=status.HTTP_200_OK)
        except Exception as exc:
            return Response({'detail': repr(exc)}, status=status.HTTP_400_BAD_REQUEST)


class FavoritesListView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, username=None, format=None):
        # Get favorite list of a user
        try:
            user = get_user(request, username)
            fav_list = FavoriteList.objects.get(user=user)
            return Response(FavoriteListSerializer(fav_list).data,
                            status=status.HTTP_200_OK)
        except Exception as exc:
            return Response({'detail': repr(exc)}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, username=None, format=None):
        # Add favorite
        try:
            assert username is None, "Trying to edit another user's following list"
            data = request.data
            posts_to_fav = Post.objects.filter(id__in=data["id"])
            user = request.user
            fav_list = FavoriteList.objects.get(user=user)
            fav_list.favorites.add(*posts_to_fav)
            fav_list.save()
            return Response({'message': 'ok'}, status=status.HTTP_200_OK)
        except Exception as exc:
            return Response({'detail': repr(exc)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, username=None, format=None):
        # Remove favorite
        try:
            assert username is None, "Trying to edit another user's following list"
            data = request.data
            posts_to_unfav = Post.objects.filter(id__in=data["id"])
            user = request.user
            fav_list = FavoriteList.objects.get(user=user)
            fav_list.favorites.remove(*posts_to_unfav)
            fav_list.save()
            return Response({'message': 'ok'}, status=status.HTTP_200_OK)
        except Exception as exc:
            return Response({'detail': repr(exc)}, status=status.HTTP_400_BAD_REQUEST)
