from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    phone = models.CharField(unique=True, max_length=35)
    address = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    is_verified = models.BooleanField(null=True, default=False, blank=True)

    def __str__(self):
        return self.username
