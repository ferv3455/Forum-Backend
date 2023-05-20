from django.contrib import admin
from .models import FollowList, FavoriteList

# Register your models here.
admin.site.register(FollowList)
admin.site.register(FavoriteList)
