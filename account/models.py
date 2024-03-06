from django.db import models
from django.contrib.auth.models import AbstractUser

from account.managers import UserManager


# User =

class User(AbstractUser):
    username = None
    phone = models.CharField(max_length=13, unique=True)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)

    USERNAME_FIELD = 'phone'
    objects = UserManager()

    def __str__(self):
        return self.phone




