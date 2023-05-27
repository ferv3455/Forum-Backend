from django.urls import path
from . import views


urlpatterns = [
    path('', views.HelloView.as_view(), name='hello'),
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('posts/<str:id>', views.PostDetailView.as_view(), name='post-detail'),
    path('image/', views.ImageView.as_view(), name='images'),
    path('image/<str:id>', views.ImageInstanceView.as_view(), name='image-instance'),
    path('like/<str:id>', views.LikeView.as_view(), name='like'),
    path('comment/<str:id>', views.CommentView.as_view(), name='comment'),
    path('comment/like/<str:id>', views.CommentLikeView.as_view(), name='comment-like'),
]
