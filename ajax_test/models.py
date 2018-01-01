from django.db import models


class Images(models.Model):
    name = models.CharField(max_length=255, default="trademark's name")
    image = models.ImageField(null=False)
