from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import LogoutView, RegisterView, CheckValidView


urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('check-valid/', CheckValidView.as_view(), name='check-validity'),
]
