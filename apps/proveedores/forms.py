from django import forms
from .models import *

class proveedorForm(forms.ModelForm):

    class Meta:
        model = Proveedor

        fields = [
            'nombre',
            'apellidos',
            'direccion',
            'mail',
            'producto',
            'telefono',
        ]

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellidos'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Direccion'}),
            'mail': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Correo electronico'}),
            'producto': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Productos'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefono'}),
        }

        labels = {
            'nombre' : 'Nombre',
            'apellidos': 'Apellidos',
            'direccion': 'Direccion',
            'mail': 'Mail',
            'producto': 'Productos',
            'telefono': 'Telefono',
        }