from django.db import models
from django.contrib.auth.models import AbstractUser

USER_TYPE = (('1', 'Business company'), ('3', 'Law firm office'))


class BlogUser(AbstractUser):
    full_name = models.CharField(max_length=120, blank=True, null=True)
    phone_number = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=False, null=True, choices=USER_TYPE, default='2')
