from django.shortcuts import render, redirect
from .models import *
from .forms import *

#Listar proveedores me reenderiza en el template denominado > listar_proveedores.html todos los proveedores
#cargados en la base de datos, en representacion "forma tabla".
def listar_proveedores(request):
    lista_proveedores = Proveedor.objects.all()
    contexto = {'proveedores': lista_proveedores}
    return render(request, 'proveedores/listar_proveedores.html', contexto)

#Eliminar proveedor recibe como parametro el "id del proveedor" que se quiere eliminar de la base de datos
#se utiliza el "redirect" para redireccionar a la lista de los proveedores.
def eliminar_proveedor(request, id_proveedor):
    thisProveedor = Proveedor.objects.get(id_proveedor=id_proveedor)
    if request.method == 'GET':
        thisProveedor.delete()
    return redirect('listar_proveedores')

#Ingresar proveedor mediante el "proveedorForm" carga los fields determinados en el form, genera un ingreso de provedor
#A la base de datos.
def ingresar_proveedor(request):
    if request.method == 'POST':
        form = proveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_proveedores')
        else:
            form = proveedorForm()
    else:
        form = proveedorForm()
    return render(request, 'proveedores/ingresar_proveedores.html', {'form': form})

def modificar_proveedor(request, id_proveedor):
    thisProveedor = Proveedor.objects.get(id=id_proveedor)
    if request.method == 'GET':
        form = proveedorForm(instance=thisProveedor)
    else:
        form = proveedorForm(request.POST, instance=thisProveedor)
        if form.is_valid():
            form.save()
        else:
            form = proveedorForm()
        return redirect('listar_proveedores')
    return render(request, 'proveedores/modificar_proveedor.html', {'form': form})
    
# thisProveedor = Proveedor.objects.get(id=id_proveedor).producto.all()