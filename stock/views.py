from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.template.loader import render_to_string
from stock.models import *
from django.middleware.csrf import get_token

# from stock.models import Stock # Esto es para importar las cosas de la bd

def index(request):
	productos = Producto.objects.filter(tipo_categoria=1)
	categorias = Categoria.objects.all()
	context = {'productos': productos, 'categorias': categorias}
	return render(request,"stock/index.html",context)

def proveedores(request):
	proveedores = Proveedor.objects.all()
	context = {'proveedores': proveedores} #agregar logica para traer proveedores
	return render(request,"stock/proveedores.html",context)

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

def modificar_producto(request):
	producto = Producto.objects.filter(codigo=request.GET['codigo'])
	producto.update(nombre=request.GET['nombre'],precio_costo=float((request.GET['precio_costo']).replace(",", ".")),precio_venta=float((request.GET['precio_venta']).replace(",", ".")))
	return redirect('index')

def agregar_proveedor(request):
	if request.method == 'POST':
		nombre = request.POST['nombre']
		apellido = request.POST['apellidos']
		direccion = request.POST['direccion']
		mail = request.POST['mail']
		proveedor = Proveedor(nombre=nombre,apellidos=apellido,direccion=direccion,mail=mail)
		proveedor.save()
	return render(request,"stock/agregarProveedor.html")


def busqueda_producto(request):
	categoria = Categoria.objects.get(descripcion_categoria=request.POST['descripcion_categoria'].strip())
	productos = Producto.objects.filter(codigo__contains=request.POST['codigo'],tipo_categoria=categoria) | Producto.objects.filter(nombre__contains=request.POST['codigo'],tipo_categoria=categoria)
	context = {'productos': productos}
	html = render_to_string('stock/filtrado.html', context)
	return HttpResponse(html)
#def prodcutos_lista(request):
#	productos = Producto.objects.all()
#	context = {'productos': productos}
#	return render(request,"stock/index.html",context)