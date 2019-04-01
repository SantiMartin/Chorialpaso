from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.template.loader import render_to_string
from stock.models import *
# from stock.models import Stock # Esto es para importar las cosas de la bd

def index(request):
	productos = Producto.objects.filter(tipo_categoria=1)
	categorias = Categoria.objects.all()
	context = {'productos': productos, 'categorias': categorias}
	return render(request,"stock/index.html",context)

def eliminar_producto(request):
	producto = Producto.objects.get(codigo= request.GET['codigo']).delete()
	response = redirect('index')
	return response

def filtrar_categoria(request):
	productos = Producto.objects.filter(tipo_categoria=request.POST['id_categoria'])
	context = {'productos': productos}
	html = render_to_string('stock/filtrado.html', context)
	return HttpResponse(html)

def agregar_producto(request):
	categorias = Categoria.objects.all()
	formatos = Formato.objects.all()
	context ={'formatos': formatos, 'categorias': categorias}
	if request.method == 'POST':
		categoria = Categoria.objects.get(id_categoria=request.POST['tipo_categoria'])
		nombre=request.POST['nombre']
		tipo_formato = Formato.objects.get(id_formato=request.POST['tipo_formato'])
		cantidad_producto = request.POST['cantidad_producto']
		precio_costo = request.POST['precio_costo']
		precio_venta = request.POST['precio_venta']
		producto = Producto(tipo_categoria=categoria,nombre=nombre,tipo_formato=tipo_formato,cantidad_producto=cantidad_producto,precio_costo=precio_costo,precio_venta=precio_venta)
		producto.save()
	return render(request,"stock/agregarProducto.html",context)
	# return HttpResponse(mi_template.render(context)) para realizar el cambio, fijarse si es lo mismo que el de arriba

	# agregar urls para que se pueda ver...

#def prodcutos_lista(request):
#	productos = Producto.objects.all()
#	context = {'productos': productos}
#	return render(request,"stock/index.html",context)