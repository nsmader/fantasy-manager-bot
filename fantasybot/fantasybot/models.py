from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    final_key = models.CharField(max_length=200)
    final_secret = models.CharField(max_length=200)
    has_authed = models.BooleanField()
