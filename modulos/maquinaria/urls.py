from django.urls import path
from modulos.maquinaria.views.maquinaria.views import *

app_name = "maquinaria"
urlpatterns = [
    path('detalle_maquinaria/', (maquinariaListView.as_view()), name='detalle_maquinaria'),
    path('crear_maquinaria/', (CrearMaquinaria.as_view()), name='crear_maquinaria'),
    path('editar_maquinaria/<int:pk>', (ActualizarMaquinaria.as_view()), name='editar_maquinaria'),
    path('eliminar_maquinaria/<int:pk>', (EliminarMaquinaria.as_view()), name='eliminar_maquinaria'),

]

