from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	context = {

	}
	return render(request,"stock/index.html",context)

def agregarProducto(request):
	context = {

	}
	return render(request,"stock/agregarProducto.html",context)