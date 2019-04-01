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
	print("entra")
	productos = Producto.objects.filter(tipo_categoria=request.POST['id_categoria'])
	context = {'productos': productos}
	print(productos)
	html = render_to_string('stock/filtrado.html', context)
	return HttpResponse(html)


	# return HttpResponse(mi_template.render(context)) para realizar el cambio, fijarse si es lo mismo que el de arriba

	# agregar urls para que se pueda ver...

#def prodcutos_lista(request):
#	productos = Producto.objects.all()
#	context = {'productos': productos}
#	return render(request,"stock/index.html",context)