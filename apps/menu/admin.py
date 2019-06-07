from django.contrib import admin
from .models import Menu, MenuxProductos
from apps.stock.models import Producto

# Register your models here.

admin.site.register(Menu)
admin.site.register(MenuxProductos)

