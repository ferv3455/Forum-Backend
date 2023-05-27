from django.contrib import admin
from .models import Tag, Image, Post, Like, Comment

# Register your models here.
admin.site.register(Tag)
admin.site.register(Image)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Comment)
