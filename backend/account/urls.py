from django.urls import path

from .views import ProfileView, UsernameView, PasswordView, FollowListView, FavoritesListView


urlpatterns = [
    # Profile
    path('profile', ProfileView.as_view(), name='own-profile'),
    path('profile/<str:username>', ProfileView.as_view(), name='profile'),
    path('username', UsernameView.as_view(), name='username'),
    path('password', PasswordView.as_view(), name='password'),

    # Following list
    path('following', FollowListView.as_view(), name='own-following'),
    path('following/<str:username>', FollowListView.as_view(), name='following'),
    path('favorites', FavoritesListView.as_view(), name='own-favorites'),
    path('favorites/<str:username>', FavoritesListView.as_view(), name='favorites'),
]
