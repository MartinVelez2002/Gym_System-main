from django import forms
from django.forms import ModelForm
from modulos.clientes.models import *

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields ='__all__'
        widgets =  {
            'nombre':forms.TextInput(attrs={'class' : 'form-control', 'placeholder':'Ingrese su nombre','id':'inputNombre' } ),
            'apellido': forms.TextInput(attrs={'class' : 'form-control', 'placeholder':'Ingrese su apellido', 'id':'inputApellido'}),
            'genero': forms.Select(attrs= {'class': 'form-control', 'placeholder':'Seleccione su género', 'id':'inputGen' }),
            'cedula': forms.TextInput(attrs=
                                        {'class':'form-control',
                                         'placeholder':'Digite su número de cédula',
                                         'id':'inputCedula',
                                         }),
            'edad': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Digite su edad', 'id':'inputEdad'}),
            'fecha_de_ingreso': forms.DateInput(attrs={'class':'form-control','id':'fechIngr'})
        }