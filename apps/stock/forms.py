from django import forms
from .models import *

class modificacionForm(forms.ModelForm):

    class Meta:
        model = Modificacion

        fields = [
            'motivo',
            'codigo',
            'cantidad',
        ]

        widgets = {
            'motivo': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Motivo'}),
            'codigo': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Producto'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad'}),
        }

        labels = {
            'motivo': 'Motivo',
            'codigo': 'Nombre producto',
            'cantidad': 'Cantidad',
        }

