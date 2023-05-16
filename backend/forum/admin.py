from django.contrib import admin
from .models import Tag, Image, Post

# Register your models here.
admin.site.register(Tag)
admin.site.register(Image)
admin.site.register(Post)
