from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('proveedores', views.proveedores, name='proveedores'),
    path('productos', views.index, name='index'),
    path('filtrar_categoria', views.filtrar_categoria, name='filtrar_categoria'),
    path('eliminar', views.eliminar_producto, name='eliminar_producto'),
    path('agregar_producto', views.agregar_producto, name='agregar_producto'),
    path('agregar_proveedor', views.agregar_proveedor, name='agregar_proveedor'),
    path('modificar_producto', views.modificar_producto, name='modificar_producto'),
    path('busqueda_producto', views.busqueda_producto, name='busqueda_producto'),
]
