from rest_framework import serializers

from authentication.models import Profile
from authentication.serializers import ProfileSerializer
from .models import Tag, Image, Comment


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name', )


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'thumbnail')


class ImageFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'content')


class PostBriefSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    title = serializers.CharField()


class PostSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    title = serializers.CharField()
    content = serializers.CharField()
    createdAt = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    user_profile = serializers.SerializerMethodField('get_user_profile')

    images = ImageSerializer(many=True)
    tags = TagSerializer(many=True)

    likes = serializers.IntegerField()
    favorites = serializers.IntegerField()
    comments = serializers.IntegerField()

    def get_user_profile(self, post):
        user = post.user
        profile = Profile.objects.get(user=user)
        return ProfileSerializer(profile).data


class PostFullSerializer(PostSerializer):
    images = ImageFullSerializer(many=True)


class LikeSerializer(serializers.Serializer):
    user_profile = serializers.SerializerMethodField('get_user_profile')
    post = PostBriefSerializer()
    createdAt = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    def get_user_profile(self, like):
        user = like.user
        profile = Profile.objects.get(user=user)
        return ProfileSerializer(profile).data


class CommentSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    user_profile = serializers.SerializerMethodField('get_user_profile')
    post = PostBriefSerializer()
    content = serializers.CharField()
    createdAt = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    likes = serializers.IntegerField()

    def get_user_profile(self, comment):
        user = comment.user
        profile = Profile.objects.get(user=user)
        return ProfileSerializer(profile).data
