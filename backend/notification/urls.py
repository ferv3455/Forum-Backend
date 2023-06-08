from django.urls import path
from . import views


urlpatterns = [
    path('messages-received/', views.MessageReceivedView.as_view(), name='received'),
    path('messages/', views.MessageView.as_view(), name='messages'),
]
