# Generated by Django 4.2.1 on 2023-05-16 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_alter_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='forum.tag'),
        ),
    ]
