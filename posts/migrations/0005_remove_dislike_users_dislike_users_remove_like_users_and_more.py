# Generated by Django 4.0.4 on 2022-04-14 06:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0004_alter_dislike_options_alter_like_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dislike',
            name='users',
        ),
        migrations.AddField(
            model_name='dislike',
            name='users',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users_dislikes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='like',
            name='users',
        ),
        migrations.AddField(
            model_name='like',
            name='users',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
