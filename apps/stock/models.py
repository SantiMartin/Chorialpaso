from django.db import models
import datetime
# Create your models here.
class Categoria(models.Model):
    descripcion_categoria = models.CharField(max_length=80, blank=False)

    def __str__(self):
        return self.descripcion_categoria

class Producto(models.Model):
    tipo_categoria = models.ForeignKey(Categoria, null=False, blank=False, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50, blank=False)
    cantidad_producto = models.IntegerField(null=False, blank=False, default=0)

    def __str__(self):
        return self.nombre

class Modificacion(models.Model):
    motivo = models.CharField(max_length=80, blank=False)
    fecha = models.DateField(default=datetime.date.today)
    codigo = models.ForeignKey(Producto, null=False, blank=False, on_delete=models.CASCADE)
    cantidad = models.IntegerField(null=False, blank=False, default=0)

    def __str__(self):
        return self.motivo
