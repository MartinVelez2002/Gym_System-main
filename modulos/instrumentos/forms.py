from django.forms import ModelForm
from django import forms
from modulos.instrumentos.models import *


class InstrumentosForm(ModelForm):
    class Meta:
        model = Instrumento
        fields = '__all__'
        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese nombre del instrumento'}),
            'peso': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el Peso'}),
            'precio_instrumento': forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Ingrese el precio del instrumento'}),
            'fecha_compra_instrumento': forms.DateInput(format=('%Y-%m-%d'),
                                                       attrs={'class': 'form-control', 'type': 'date', 'id':'fecha'}),
            'unidades': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad del instrumento'}),
        }