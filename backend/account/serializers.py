from rest_framework import serializers

from authentication.models import Profile
from authentication.serializers import UserSerializer, ProfileSerializer
from forum.serializers import PostSerializer


class FollowListSerializer(serializers.Serializer):
    user = UserSerializer()
    following = serializers.SerializerMethodField('get_user_profiles')

    def get_user_profiles(self, follow_list):
        following_users = follow_list.following
        following_profiles = Profile.objects.filter(user__in=following_users.all())
        return ProfileSerializer(following_profiles, many=True).data


class FavoriteListSerializer(serializers.Serializer):
    user = UserSerializer()
    favorites = PostSerializer(many=True)
