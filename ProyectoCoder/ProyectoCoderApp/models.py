from django.db import models

# Create your models here.

class Vehiculo(models.Model):
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    anio = models.IntegerField()
    
    
    
class Repuesto(models.Model):
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    
    
    
class Accesorio(models.Model):
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    precio = models.IntegerField()
    
