# Create your models here.
from django.db import models
from apps.stock.models import Producto

# Create your models here.

class Menu(models.Model):    
    nombre = models.CharField(max_length=50, blank=False)
    precio_venta = models.FloatField(max_length=50, blank=False)
    menuxProductos= models.ManyToManyField(   
    	Producto,
        through='MenuxProductos',
        through_fields=('menu', 'producto'),
    )
    def __str__(self):
        return self.nombre

class MenuxProductos(models.Model):
	menu= models.ForeignKey(Menu, null=False, blank=False, on_delete=models.CASCADE)
	producto = models.ForeignKey(Producto, null=False, blank=False, on_delete=models.CASCADE)
	cantidad = models.IntegerField(null=False, blank=False)
	def __str__(self):
		nombre=str(self.producto) + " en " + str(self.menu)
		return str(nombre)