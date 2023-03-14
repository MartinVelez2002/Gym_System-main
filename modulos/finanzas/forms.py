from django.db import models
from django import forms
from django.utils import timezone
from django.forms import ModelForm

from modulos.finanzas.models import *


class FormFinanzas(ModelForm):
    class Meta:
        model = Finanzas
        fields = '__all__'
        widgets = {
            'personasIngresadas': forms.NumberInput(attrs={'class': 'form-control', 'id': 'personasIngresadas'}),
            'mensualidades': forms.NumberInput(
                attrs={'class': 'form-control', 'id': 'mensualidades', 'disabled': 'True'}),
            'ingresos': forms.NumberInput(attrs={'class': 'form-control', 'id': 'ingresos', 'disabled': 'True'}),
            'gastos': forms.NumberInput(attrs={'class': 'form-control', 'id': 'gastos', 'disabled': 'True'}),
            'ganancias': forms.NumberInput(attrs={'class': 'form-control', 'id': 'ganancias', 'disabled': 'True'}),
        }
