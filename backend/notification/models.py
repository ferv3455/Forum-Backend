from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Message(models.Model):
    fromUser = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='from_user')
    toUser = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='to_user')
    content = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    received = models.BooleanField(default=False)

    def __str__(self):
        return f"<Message {self.fromUser}-{self.toUser}: {self.content}>"
