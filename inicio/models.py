from django.db import models

# Create your models here.
class Producto(models.Model):
    prod_id = models.IntegerField()
    nombre = models.CharField(max_length = 20)
    marca = models.CharField(max_length = 20)
    precio = models.FloatField()
    
    def __str__(self):
        return f'{self.nombre} {self.marca} [{self.prod_id}]: $ {self.precio}'
    
class Cliente(models.Model):
    nombre = models.CharField(max_length = 20)
    apellido = models.CharField(max_length = 20)
    telefono = models.IntegerField()
    
    def __str__(self):
        return f'{self.nombre} {self.apellido} Tel: {self.telefono}'