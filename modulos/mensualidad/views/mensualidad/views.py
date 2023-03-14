from django.urls import reverse_lazy

from modulos.mensualidad.models import *
from django.views.generic import *
from modulos.mensualidad.forms import *
from django.contrib.auth.mixins import LoginRequiredMixin

class detalleMensualidad(LoginRequiredMixin, ListView):
    template_name = 'detalleMensualidad.html'
    context_object_name = 'mensualidad'
    model = Mensualidad
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get("query")
        print(query)
        if query:
            return self.model.objects.filter(cliente__nombre__icontains=query)
        else:
            return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_anterior'] = "/"
        context['listar_url'] = '/mensualidad/menu/'
        context['titulo'] = 'Registro de Mensualidad'
        context['query'] = self.request.GET.get("query") or ""
        return context


class CrearMensualidad(LoginRequiredMixin, CreateView):
    model = Mensualidad
    template_name = 'Crear_mensu.html'
    form_class = CabeceraMensual
    success_url = reverse_lazy('mensualidad:detalle_mensualidad')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear Mensualidad'
        context['action_save'] = self.request.path
        context['url_anterior'] = '/mensualidad/detalle_mensualidad/'
        context['listar_url'] = '/mensualidad/detalle_mensualidad/'

        return context


# Eliminar
class EliminarMensualidad(LoginRequiredMixin, DeleteView):
    model = Mensualidad
    template_name = 'eliminar_mensu.html'
    success_url = reverse_lazy('mensualidad:detalle_mensualidad')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Eliminar Registro de Mensualidad'
        context['url_anterior'] = '/mensualidad/detalle_mensualidad/'
        context['listar_url'] = '/mensualidad/detalle_mensualidad/'
        return context


# Actualizar
class ActualizarMensualidad(LoginRequiredMixin, UpdateView):
    model = Mensualidad
    template_name = 'editar_mensu.html'
    success_url = reverse_lazy('mensualidad:detalle_mensualidad')
    form_class = CabeceraMensual

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Actualizar Datos de la mensualidad'
        context['url_anterior'] = '/mensualidad/detalle_mensualidad/'
        context['listar_url'] = '/mensualidad/detalle_mensualidad/'
        return context
