from rest_framework import serializers

from authentication.models import Profile
from authentication.serializers import ProfileSerializer
from forum.serializers import LikeSerializer, CommentSerializer


class MessageSerializer(serializers.Serializer):
    fromUser = serializers.SerializerMethodField('get_user_profile')
    toUser = serializers.SerializerMethodField('get_receiver_profile')
    content = serializers.CharField()
    createdAt = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    def get_user_profile(self, comment):
        user = comment.fromUser
        profile = Profile.objects.get(user=user)
        return ProfileSerializer(profile).data

    def get_receiver_profile(self, comment):
        user = comment.toUser
        profile = Profile.objects.get(user=user)
        return ProfileSerializer(profile).data


class LikeMessageSerializer(serializers.Serializer):
    like = LikeSerializer()


class CommentMessageSerializer(serializers.Serializer):
    comment = CommentSerializer()
