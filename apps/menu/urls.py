from django.urls import path
from django.views.decorators.csrf import csrf_exempt, requires_csrf_token

from . import views

urlpatterns = [    
    path('listar_menu', views.listar_menu, name='listar_menu'),
    path('modificar_menu/<int:id_menu>', views.modificar_menu, name='modificar_menu'),
    #Defino url para eliminar menu.

]
