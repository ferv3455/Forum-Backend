import datetime

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from notification.models import Message
from notification.serializers import MessageSerializer


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
