from django.db import models
from apps.stock.models import Producto
# Create your models here.

class Proveedor(models.Model):
    nombre = models.CharField(max_length=80, blank=False)
    apellidos = models.CharField(max_length=80, blank=False)
    direccion = models.CharField(max_length=110, blank=False)
    mail = models.EmailField(blank=True)
    producto = models.ManyToManyField(Producto)
    telefono = models.CharField(unique=True,max_length=20, blank=False)

    def __str__(self):
        proveedor = self.nombre + " " + self.apellidos
        return proveedor
