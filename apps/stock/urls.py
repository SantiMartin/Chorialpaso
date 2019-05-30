from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    #Defino url para listar productos.
    path('listar_stock', views.listar_stock, name='listar_stock'),
    #Defino url para bajar unidades de stock de un determinado producto.
    path('baja_stock', views.baja_stock, name='baja_stock'),
    #Defino url para listar todos los movimientos
    path('listar_movimientos', views.listar_movimientos, name='listar_movimientos'),
]
