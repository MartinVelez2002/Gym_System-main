from django.urls import path
from modulos.instrumentos.views.instrumentos.views import *

app_name = "instrumentos"
urlpatterns = [
    path('detalle_instrumento/', (Detalle_Instrumentos.as_view()), name='detalle_instrumento'),
    path('crear_instrumento/', (Añadir_Instrumento.as_view()), name='crear_instrumento'),
    path('editar_instrumento/<int:pk>', (Actualizar_Instrumento.as_view()), name='editar_instrumento'),
    path('eliminar_instrumento/<int:pk>', (Eliminar_Instrumento.as_view()), name='eliminar_instrumento'),

]