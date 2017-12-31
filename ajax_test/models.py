from django.db import models


class Demo(models.Model):
    name = models.CharField(max_length=255, default="demo")
    image = models.ImageField(null=False)
