from django import forms
from .models import Menu

class MenuForm(forms.ModelForm):

    class Meta:
        model = Menu

        fields = [
            'nombre',
            'precio_venta',
        ]

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'precio_venta': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio'}),
        }

        labels = {
            'nombre' : 'Nombre',
            'precio_venta': 'Precio',
        }