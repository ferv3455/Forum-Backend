from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from authentication.models import Profile
from forum.models import Post


# Create your models here.
class FollowList(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE, related_name='follow_owner')
    following = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return f"<FollowList: user {self.user}>"


class FavoriteList(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE, related_name='fav_owner')
    favorites = models.ManyToManyField(Post, blank=True)

    def __str__(self):
        return f"<Favorite-list: user {self.user}>"


# Auto create two instances of the models above
@receiver(post_save, sender=get_user_model())
def create_account(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        FollowList.objects.create(user=instance)
        FavoriteList.objects.create(user=instance)
