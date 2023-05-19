from django.contrib import admin
from .models import Profile, FollowList, FavoriteList

# Register your models here.
admin.site.register(Profile)
admin.site.register(FollowList)
admin.site.register(FavoriteList)
