from rest_framework import serializers

from forum.serializers import UserSerializer, PostSerializer


class ProfileSerializer(serializers.Serializer):
    user = UserSerializer()
    avatar = serializers.CharField()
    description = serializers.CharField()


class FollowListSerializer(serializers.Serializer):
    user = UserSerializer()
    following = UserSerializer(many=True)


class FavoriteListSerializer(serializers.Serializer):
    user = UserSerializer()
    favorites = PostSerializer(many=True)
