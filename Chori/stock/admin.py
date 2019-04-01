from django.contrib import admin
from .models import Producto, Categoria, ProductoXProveedor, Proveedor, Formato, Contacto
# Register your models here.

#admin.site.register(Producto)
#admin.site.register(Categoria)
admin.site.register(ProductoXProveedor)
admin.site.register(Proveedor)
#admin.site.register(Formato)
admin.site.register(Contacto)

class ProductoAdmin(admin.ModelAdmin):
    """list_display agrega atributos en la lista de autores mostrada"""
    list_display = ('codigo','tipo_categoria','nombre','cantidad_producto','tipo_formato','precio_costo', 'precio_venta')
    """fields me cambia cuando quiero editar los datos del autor, me indica que campos se va a modificar"""
    fields = ['tipo_categoria','nombre','cantidad_producto','tipo_formato', 'precio_costo', 'precio_venta']

class CategoriaAdmin(admin.ModelAdmin):
    """list_display agrega atributos en la lista de autores mostrada"""
    list_display = ('id_categoria','descripcion_categoria')
    """fields me cambia cuando quiero editar los datos del autor, me indica que campos se va a modificar"""
    fields = ['descripcion_categoria']

class FormatoAdmin(admin.ModelAdmin):
    """list_display agrega atributos en la lista de autores mostrada"""
    list_display = ('id_formato','descripcion_formato')
    """fields me cambia cuando quiero editar los datos del autor, me indica que campos se va a modificar"""
    fields = ['descripcion_formato']

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Formato, FormatoAdmin)