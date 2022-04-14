from django.db import models
# from django.dispatch import receiver
# from django.core.signals import request_finished
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    last_activity = models.DateTimeField(default=timezone.now)

