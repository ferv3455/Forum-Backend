from django.contrib import admin

from notification.models import Message, LikeMessage, CommentMessage

# Register your models here.
admin.site.register(Message)
admin.site.register(LikeMessage)
admin.site.register(CommentMessage)
