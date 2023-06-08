import datetime
import traceback

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from notification.models import Message, LikeMessage, CommentMessage
from notification.serializers import MessageSerializer, LikeMessageSerializer, CommentMessageSerializer


# Create your views here.
class MessageReceivedView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        # Send the time before which all messages have been received
        try:
            user = request.user
            time = datetime.datetime.strptime(request.data['time'], '%Y-%m-%d %H:%M:%S')
            received_messages = Message.objects.filter(received=False, toUser=user, createdAt__lt=time)
            received_messages.update(received=True)
            return Response({'message': 'ok'}, status=status.HTTP_200_OK)
        except Exception as exc:
            return Response({'detail': repr(exc)}, status=status.HTTP_400_BAD_REQUEST)


class MessageView(APIView):
    def get(self, request):
        # Get all unreceived message
        try:
            user = request.user
            query_result = Message.objects.filter(toUser=user, received=False)
            return Response(MessageSerializer(query_result, many=True).data, status=status.HTTP_200_OK)
        except Exception as exc:
            return Response({'detail': repr(exc)}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        # Send a message
        try:
            fromUser = request.user
            toUser = User.objects.get(username=request.data['user'])
            content = request.data['content']
            Message.objects.create(fromUser=fromUser, toUser=toUser, content=content)
            return Response({'message': 'ok'}, status=status.HTTP_200_OK)
        except Exception as exc:
            return Response({'detail': repr(exc)}, status=status.HTTP_400_BAD_REQUEST)


class LikeMessageReceivedView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        # Send the time before which all messages have been received
        try:
            user = request.user
            time = datetime.datetime.strptime(request.data['time'], '%Y-%m-%d %H:%M:%S')
            received_messages = \
                LikeMessage.objects.filter(received=False, like__post__user=user, like__createdAt__lt=time)
            received_messages.delete()
            return Response({'message': 'ok'}, status=status.HTTP_200_OK)
        except Exception as exc:
            return Response({'detail': repr(exc)}, status=status.HTTP_400_BAD_REQUEST)


class LikeMessageView(APIView):
    def get(self, request):
        # Get all unreceived message
        try:
            user = request.user
            query_result = LikeMessage.objects.filter(received=False, like__post__user=user)
            result = LikeMessageSerializer(query_result, many=True).data
            return Response([x['like'] for x in result], status=status.HTTP_200_OK)
        except Exception as exc:
            traceback.print_exc()
            return Response({'detail': repr(exc)}, status=status.HTTP_400_BAD_REQUEST)


class CommentMessageReceivedView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        # Send the time before which all messages have been received
        try:
            user = request.user
            time = datetime.datetime.strptime(request.data['time'], '%Y-%m-%d %H:%M:%S')
            received_messages = \
                CommentMessage.objects.filter(received=False, comment__post__user=user, comment__createdAt__lt=time)
            received_messages.delete()
            return Response({'message': 'ok'}, status=status.HTTP_200_OK)
        except Exception as exc:
            return Response({'detail': repr(exc)}, status=status.HTTP_400_BAD_REQUEST)


class CommentMessageView(APIView):
    def get(self, request):
        # Get all unreceived message
        try:
            user = request.user
            query_result = CommentMessage.objects.filter(received=False, comment__post__user=user)
            result = CommentMessageSerializer(query_result, many=True).data
            return Response([x['comment'] for x in result], status=status.HTTP_200_OK)
        except Exception as exc:
            return Response({'detail': repr(exc)}, status=status.HTTP_400_BAD_REQUEST)
