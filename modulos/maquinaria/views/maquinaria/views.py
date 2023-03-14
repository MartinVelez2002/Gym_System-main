from django.urls import reverse_lazy
from django.views.generic import *
from modulos.maquinaria.models import *
from modulos.maquinaria.forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
class maquinariaListView(LoginRequiredMixin, ListView):
    template_name = "maquinaria/detalle_maquinaria.html"
    model = Maquinaria
    context_object_name = 'maquinaria'
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get("query")
        print(query)
        if query:
            return self.model.objects.filter(Descripcion__icontains=query)
        else:
            return self.model.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['crear_url'] = 'crearmaquinaria/'
        mant = context['maquinaria']
        estados = ['Bajo Mantenimiento' if s.Mantenimiento else 'Disponible' for s in mant]
        context['estado_guardado'] = zip(mant, estados)
        context['query'] = self.request.GET.get("query") or ""
        return context

class CrearMaquinaria(LoginRequiredMixin, CreateView):
    model = Maquinaria
    template_name = "maquinaria/añadir_maquinaria.html"
    success_url = reverse_lazy('maquinaria:detalle_maquinaria')
    form_class = MaquinariaForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Añadir Maquinaria'
        context['url_anterior'] = '/maquinaria/detalle_maquinaria/'
        context['listar_url'] = '/maquinaria/detalle_maquinaria/'
        return context

class ActualizarMaquinaria(LoginRequiredMixin, UpdateView):
    model = Maquinaria
    template_name = "maquinaria/editar_maquinaria.html"
    success_url = reverse_lazy('maquinaria:detalle_maquinaria')
    form_class = MaquinariaForm


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Editar Maquinaria'
        context['url_anterior'] = '/maquinaria/detalle_maquinaria/'
        return context

class EliminarMaquinaria(LoginRequiredMixin, DeleteView):
    model = Maquinaria
    template_name = "maquinaria/eliminar_maquinaria.html"
    success_url = reverse_lazy('maquinaria:detalle_maquinaria')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Eliminar Maquinaria'
        context['url_anterior'] = '/maquinaria/detalle_maquinaria/'
        return context