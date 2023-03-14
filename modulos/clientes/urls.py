
from django.urls import path
from modulos.clientes.views.cliente.views import *


app_name = "clientes"
urlpatterns = [
    path('detalle_cliente/', (DetalleCliente.as_view()), name='detalle_cliente'),
    path('crear_cliente/', (Addcliente.as_view()), name='crear_cliente'),
    path('editar_cliente/<int:pk>', (EditarCliente.as_view()), name='editar_cliente'),
    path('eliminar_cliente/<int:pk>', (EliminarCliente.as_view()), name='eliminar_cliente'),

]
