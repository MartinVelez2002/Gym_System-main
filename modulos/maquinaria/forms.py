from django import forms
from django.forms import ModelForm
from modulos.maquinaria.models import *

class MaquinariaForm(ModelForm):
    class Meta:
        model = Maquinaria
        fields = '__all__'
        exclude=['usuario']

        widgets = {
            'Descripcion': forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingrese nombre de la Maquina'}),
            'Cantidad': forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingrese la Cantidad'}),
            'precio_maquinaria': forms.NumberInput(attrs={'class': 'form-control','placeholder':'Ingrese precio de la maquinaria'}),
            'fecha_compra_maquinaria': forms.DateInput(format=('%Y-%m-%d'),
                                                       attrs={'class': 'form-control', 'type': 'date', 'id':'fecha'}),
            'Mantenimiento': forms.CheckboxInput()
        }