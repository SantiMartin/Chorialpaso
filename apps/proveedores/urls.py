from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    #Defino url para ingresar un proveedor.
    path('ingresar_proveedor', views.ingresar_proveedor, name='ingresar_proveedor'),
    #Defino url para listar proveedores.
    path('listar_proveedores', views.listar_proveedores, name='listar_proveedores'),
    #Defino url para eliminar proveedor.
    path('eliminar_proveedor/<int:id_proveedor>', views.eliminar_proveedor, name='eliminar_proveedor'),
    #Defino url para modificar proveedor.
    path('modificar_proveedor/<int:id_proveedor>', views.modificar_proveedor, name='modificar_proveedor'),
]
