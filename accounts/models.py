from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    rate = models.SmallIntegerField(blank=True, default=0)
    reviews = models.SmallIntegerField(blank=True, default=0)
    telephone = models.IntegerField(blank=True, default=0)
    lat = models.DecimalField(max_digits=19, decimal_places=16)
    lng = models.DecimalField(max_digits=19, decimal_places=16)
    radius = models.SmallIntegerField(blank=True, default=0)