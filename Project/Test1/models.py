from django.db import models
# Create your models here.

class Carnet(models.Model):
    Rut = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=200)
    Apellido_P = models.CharField(max_length=200)
    Apellido_M =models.CharField(max_length=200)
    Tel = models.IntegerField()
