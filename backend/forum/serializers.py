from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Tag, Image


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', )


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


class PostSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    title = serializers.CharField()
    content = serializers.CharField()
    createdAt = serializers.DateTimeField()
    user = UserSerializer()

    images = ImageSerializer(many=True)
    tags = TagSerializer(many=True)

    likes = serializers.IntegerField()
    favorites = serializers.IntegerField()
    comments = serializers.IntegerField()


class PostFullSerializer(PostSerializer):
    images = ImageFullSerializer(many=True)
