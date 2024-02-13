from django.db import models


class VCardModel(models.Model):
    name = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)