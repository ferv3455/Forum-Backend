from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class ProfileSerializer(serializers.Serializer):
    user = UserSerializer()
    avatar = serializers.CharField()
    description = serializers.CharField()
