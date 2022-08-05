from django.db import models
from django.utils import timezone

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    avatar = models.ImageField(
        upload_to='images/',
        blank=True,
        null=True
    )
    last_action=models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.username



