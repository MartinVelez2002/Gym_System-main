from django.urls import reverse_lazy
from django.views.generic import *
from modulos.instrumentos.models import *
from modulos.instrumentos.forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
class Detalle_Instrumentos(LoginRequiredMixin, ListView):
    template_name = "instrumentos/detalle_instrumentos.html"
    model = Instrumento
    context_object_name = 'instrumentos'
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get("query")
        print(query)
        if query:
            return self.model.objects.filter(descripcion__icontains=query)
        else:
            return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Instrumentos'
        context['query'] = self.request.GET.get("query") or ""
        return context


class Añadir_Instrumento(LoginRequiredMixin, CreateView):
    model = Instrumento
    template_name = "instrumentos/añadir_instrumento.html"
    success_url = reverse_lazy('instrumentos:detalle_instrumento')
    form_class = InstrumentosForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Instrumentos'
        context['url_anterior'] = '/instrumentos/detalle_instrumento'
        return context


class Actualizar_Instrumento(LoginRequiredMixin, UpdateView):
    model = Instrumento
    template_name = "instrumentos/editar_instrumento.html"
    success_url = reverse_lazy('instrumentos:detalle_instrumento')
    form_class = InstrumentosForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Edición de Instrumentos'
        context['url_anterior'] = '/instrumentos/detalle_instrumento'
        return context


class Eliminar_Instrumento(LoginRequiredMixin, DeleteView):
    model = Instrumento
    template_name = "instrumentos/eliminar_instrumento.html"
    success_url = reverse_lazy('instrumentos:detalle_instrumento')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Eliminar Instrumentos'
        context['url_anterior'] = '/instrumentos/detalle_instrumento'
        return context
