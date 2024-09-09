from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    bio = models.TextField(null=True, blank=True)
    profile_picture = models.TextField(blank=True)
    background_picture = models.TextField(blank=True)

    def __str__(self):
        return self.username
