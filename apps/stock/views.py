from django.shortcuts import render, redirect
from .models import *
from .forms import *

#Listar productos me reenderiza en el template denominado > listar_productos.html todos los productos
#cargados en la base de datos, en representacion "forma tabla".
def listar_stock(request):
    lista_stock = Producto.objects.all()
    contexto = {'productos': lista_stock}
    return render(request, 'stock/listar_stock.html', contexto)

def baja_stock(request):
    if request.method == 'POST':
        form = modificacionForm(request.POST)
        if form.is_valid():
            modificacion = form.save()
            producto = Producto.objects.get(id=modificacion.codigo.id)
            cantidad_vieja = producto.cantidad_producto
            cantidad_nueva = cantidad_vieja - modificacion.cantidad
            producto.cantidad_producto = cantidad_nueva
            producto.save(update_fields=["cantidad_producto"])
            return redirect('listar_stock')
        else:
            form = modificacionForm()
    else:
        form = modificacionForm()
    return render(request, 'stock/baja_stock.html', {'form': form})

def listar_movimientos(request):
    listar_movimientos = Modificacion.objects.all()
    contexto = {'listar_movimientos': listar_movimientos}
    return render(request, 'stock/listar_movimientos.html', contexto)
