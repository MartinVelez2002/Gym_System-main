from django.urls import path
from modulos.finanzas.views.finanzas.views import *


app_name = "finanzas"
urlpatterns = [
    path('detalle_finanzas/', (DetalleFinanzas.as_view()), name='detalle_finanzas'),
    path('crear_finanzas/', (RellenarFinanza.as_view()), name='crear_finanzas'),
    path('editar_finanzas/<int:pk>', (EditarFinanzas.as_view()), name='editar_finanzas'),
    path('eliminar_finanzas/<int:pk>', (EliminarFinanzas.as_view()), name='eliminar_finanzas'),

]