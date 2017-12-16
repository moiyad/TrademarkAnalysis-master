from django.db import models


# Create your models here.
class Trademark(models.Model):
    name = models.CharField(max_length=120, blank=False, null=False)
    image = models.FileField(blank=False, null=False)
    goodsand_services = models.CharField(max_length=255, blank=False, null=False)
    owner_name = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.name
