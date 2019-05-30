from django.shortcuts import render, redirect

#Inicio
def inicio(request):
    return render(request, 'base.html', {})