from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from forum.models import Like, Comment


# Create your models here.
class Message(models.Model):
    fromUser = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='from_user')
    toUser = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='to_user')
    content = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    received = models.BooleanField(default=False)

    def __str__(self):
        return f"<Message {self.fromUser}-{self.toUser}: {self.content}>"


class LikeMessage(models.Model):
    like = models.OneToOneField(Like, primary_key=True, on_delete=models.CASCADE)
    received = models.BooleanField(default=False)

    def __str__(self):
        return f"<LikeMessage {self.like}>"


class CommentMessage(models.Model):
    comment = models.OneToOneField(Comment, primary_key=True, on_delete=models.CASCADE)
    received = models.BooleanField(default=False)

    def __str__(self):
        return f"<CommentMessage {self.comment}>"


@receiver(post_save, sender=Like)
def create_account(sender, instance, created, **kwargs):
    if created:
        LikeMessage.objects.create(like=instance)


@receiver(post_save, sender=Comment)
def create_account(sender, instance, created, **kwargs):
    if created:
        CommentMessage.objects.create(comment=instance)

