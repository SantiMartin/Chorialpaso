from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('filtrar_categoria', views.filtrar_categoria, name='filtrar_categoria'),
    path('eliminar', views.eliminar_producto, name='eliminar_producto'),
    path('agregar_producto', views.agregar_producto, name='agregar_producto'),
]
