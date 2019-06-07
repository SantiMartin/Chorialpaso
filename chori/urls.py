"""chori URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    #Modo inicio cuando pones 127. sin ninguna ruta
    path('', views.inicio, name='inicio'),
    #Rutas de admin definidas por default
    path('admin/', admin.site.urls),
    #Conjunto de URL de la app proveedor
    path('proveedores/',include('apps.proveedores.urls')),
    #Conjunto de URL de la app productos
    path('stock/',include('apps.stock.urls')),
    #Conjunto de URL de la app menu
    path('menu/',include('apps.menu.urls')),

]
