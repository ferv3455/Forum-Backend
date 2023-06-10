from django.urls import path
from . import views


urlpatterns = [
    path('<str:id>', views.preview, name='preview-post'),
]
