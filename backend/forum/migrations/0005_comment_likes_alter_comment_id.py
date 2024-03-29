# Generated by Django 4.2.1 on 2023-05-27 15:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_alter_comment_post_alter_like_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this comment', primary_key=True, serialize=False),
        ),
    ]
