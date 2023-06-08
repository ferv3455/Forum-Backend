from django.urls import path
from . import views


urlpatterns = [
    path('messages-received/', views.MessageReceivedView.as_view(), name='received-msg'),
    path('messages/', views.MessageView.as_view(), name='messages'),
    path('likes-received/', views.LikeMessageReceivedView.as_view(), name='received-likes'),
    path('likes/', views.LikeMessageView.as_view(), name='likes'),
    path('comments-received/', views.CommentMessageReceivedView.as_view(), name='received-comments'),
    path('comments/', views.CommentMessageView.as_view(), name='comments'),
]
