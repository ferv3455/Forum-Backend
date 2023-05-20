from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    avatar = models.TextField(default="")
    description = models.TextField(default="")

    def __str__(self):
        return f"<Profile: user {self.user}>"
