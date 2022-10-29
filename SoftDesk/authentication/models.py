from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    user_id = models.IntegerField(blank=False, null=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=400, blank=True)
    password = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.first_name
