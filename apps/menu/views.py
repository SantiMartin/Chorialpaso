from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from .models import Menu, MenuxProductos
from .forms import MenuForm
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt,requires_csrf_token





# Create your views here.
@csrf_exempt
@requires_csrf_token
def listar_menu(request):
    lista_menues = Menu.objects.all()
    productosxMenu= MenuxProductos.objects.all()
    contexto = {'menues': lista_menues, 'productosxMenu':productosxMenu}
    return render(request, 'menu/listar_menu.html', contexto)	

@csrf_exempt
@requires_csrf_token
def modificar_menu(request, id_menu):
    print(id_menu)
    thisMenu = Menu.objects.get(id=id_menu)
    form = MenuForm(instance=thisMenu)
    if request.method == 'GET':
        form = MenuForm(instance=thisMenu)
    else:
        form = MenuForm(request.POST, instance=thisMenu)
        if form.is_valid():
            form.save()
        else:
            form = MenuForm()
        return redirect(listar_menu)
    return render(request, 'menu/modificar_menu.html', {'form': form, 'id_menu':id_menu})
