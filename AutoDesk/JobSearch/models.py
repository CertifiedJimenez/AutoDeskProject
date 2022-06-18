from django.db import models
from django.forms import CharField, FloatField

# Create your models here.
class Geocordinates(models.Model):
    location = CharField(max_length=2080)
    latitude = FloatField()
    longitude = FloatField()
