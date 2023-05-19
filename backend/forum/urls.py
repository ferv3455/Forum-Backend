from django.urls import path
from . import views


urlpatterns = [
    path('', views.HelloView.as_view(), name='hello'),
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('posts/<str:id>', views.PostDetailView.as_view(), name='post-detail'),
    path('image/', views.ImageView.as_view(), name='images'),
    path('image/<str:id>', views.ImageInstanceView.as_view(), name='image-instance'),
]
