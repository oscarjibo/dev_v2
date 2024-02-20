from django.db import models
from django.db.models import PositiveSmallIntegerField

# Create your models here.
class data(models.Model):
    nombre = models.CharField(max_length = 30)
    clave = models.IntegerField()
