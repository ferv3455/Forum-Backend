from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response({'message': 'ok'}, status=status.HTTP_200_OK)


class RegisterView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        data = request.data
        try:
            user = User.objects.create_user(username=data['username'], password=data['password'])
            token = Token.objects.create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        except Exception as exc:
            return Response({'detail': repr(exc)}, status=status.HTTP_400_BAD_REQUEST)


class CheckValidView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        return Response({'message': 'ok'}, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        return Response({'message': 'ok'}, status=status.HTTP_200_OK)
