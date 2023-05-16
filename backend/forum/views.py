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
        query_results = Post.objects.all()
        return Response(PostSerializer(query_results, many=True).data,
                        status=status.HTTP_200_OK)

    def post(self, request, format=None):
        # Add a new post
        data = request.data
        try:
            # user = User.objects.create_user(username=data['username'], password=data['password'])
            # token = Token.objects.create(user=user)
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
