from django.urls import path
from modulos.mensualidad.views.mensualidad.views import *


app_name = "mensualidad"
urlpatterns = [
    path('detalle_mensualidad/',(detalleMensualidad.as_view()), name='detalle_mensualidad'),
    path('crear_mensualidad/',(CrearMensualidad.as_view()), name='crear_mensualidad'),
    path('editar_mensualidad/<int:pk>',(ActualizarMensualidad.as_view()), name='editar_mensualidad'),
    path('eliminar_mensualidad/<int:pk>',(EliminarMensualidad.as_view()), name='eliminar_mensualidad'),

]