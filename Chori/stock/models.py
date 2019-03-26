from django.db import models

# Create your models here.

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True,unique=True)
    descripcion_categoria = models.CharField(max_length=80, blank=False)

    def __str__(self):
        return self.descripcion_categoria

class Formato(models.Model):
    id_formato = models.AutoField(primary_key=True,unique=True)
    descripcion_formato = models.CharField(max_length=80, blank=False)

    def __str__(self):
        return self.descripcion_formato

class Producto(models.Model):
    codigo = models.AutoField(primary_key=True, unique=True)
    #Relacionado con la categoria
    tipo_categoria = models.ForeignKey(Categoria, null=False, blank=False, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50, blank=False)
    #Relacionado con formato
    tipo_formato = models.ForeignKey(Formato, null=False, blank=False, on_delete=models.CASCADE)
    cantidad_producto = models.IntegerField(null=False, blank=False)
    precio_costo = models.FloatField(null=False, blank=False)
    precio_venta = models.FloatField(null=False,blank=False)

    def __str__(self):
        return self.nombre

class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True,unique=True)
    nombre = models.CharField(max_length=80, blank=False)
    apellidos = models.CharField(max_length=80, blank=False)
    direccion = models.CharField(max_length=110, blank=False)
    mail = models.EmailField(blank=True)

    def __str__(self):
        return self.nombre

class Contacto(models.Model):
    telefono = models.CharField(primary_key=True,unique=True,max_length=20)
    id_proveedor = models.ForeignKey(Proveedor, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.telefono

class ProductoXProveedor(models.Model):
    id_producto = models.ForeignKey(Producto, null=False, blank=False, on_delete=models.CASCADE)
    id_proveedor = models.ForeignKey(Proveedor, null=False, blank=False, on_delete=models.CASCADE)
    cantidad = models.IntegerField(null=False, blank=False)
    costo = models.FloatField(null=False, blank=False)
    fecha_entrada = models.DateField(null=False, blank=False)

    def __str__(self):
        return self.id_producto

