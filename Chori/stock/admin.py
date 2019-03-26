from django.contrib import admin
from .models import Producto, Categoria, ProductoXProveedor, Proveedor, Formato, Contacto
# Register your models here.

#admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(ProductoXProveedor)
admin.site.register(Proveedor)
admin.site.register(Formato)
admin.site.register(Contacto)

class ProductoAdmin(admin.ModelAdmin):
    """list_display agrega atributos en la lista de autores mostrada"""
    list_display = ('codigo','tipo_categoria','nombre','cantidad_producto',
                    'cantidad_producto','precio_costo', 'precio_venta')
    """fields me cambia cuando quiero editar los datos del autor, me indica que campos se va a modificar"""
    fields = ['nombre']

admin.site.register(Producto, ProductoAdmin)
