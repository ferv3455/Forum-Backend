# Generated by Django 4.2.1 on 2023-05-16 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_post_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='thumbnail',
            field=models.TextField(default=''),
        ),
    ]
