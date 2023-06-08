# Generated by Django 4.2.1 on 2023-05-27 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_like_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='commented_post', to='forum.post'),
        ),
        migrations.AlterField(
            model_name='like',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='liked_post', to='forum.post'),
        ),
    ]