import uuid

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Tag(models.Model):
    name = models.CharField(primary_key=True, max_length=32, help_text='Enter a tag name')

    def __str__(self):
        return f"<Tag {self.name}>"


class Image(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this image')
    content = models.TextField()
    thumbnail = models.TextField(default="")

    def __str__(self):
        return f"<Image {self.id}>"


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this post')
    title = models.CharField(max_length=256)
    content = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    images = models.ManyToManyField(Image, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    likes = models.IntegerField(default=0)
    favorites = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)

    def __str__(self):
        return f"<Post-{self.user} {self.title}>"
