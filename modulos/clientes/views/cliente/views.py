from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import *
from modulos.clientes.models import *
from modulos.clientes.forms import *
from django.contrib.auth.mixins import LoginRequiredMixin

class DetalleCliente(LoginRequiredMixin, ListView):
    template_name = 'cliente/detalle_cliente.html'
    context_object_name = 'clientes'
    model = Cliente
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get("query")
        if query:
            parts = query.split()
            if len(parts) > 1:
                nombre = parts[0]
                apellido = ' '.join(parts[1:])
                return self.model.objects.filter(
                    nombre__icontains=nombre, apellido__icontains=apellido
                )
            else:
                return self.model.objects.filter(
                    Q(nombre__icontains=query) | Q(apellido__icontains=query)
                ) | self.model.objects.filter(cedula__icontains=query)
        else:
            return self.model.objects.all()


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Registro de clientes'

        return context


class Addcliente(LoginRequiredMixin, CreateView):
    model = Cliente
    template_name = 'cliente/añadir_cliente.html'
    form_class = ClienteForm
    success_url = reverse_lazy("clientes:detalle_cliente")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Añadir Clientes'
        context['action_save'] = self.request.path
        context['url_anterior'] = '/clientes/detalle_cliente/'

        return context


class EditarCliente(LoginRequiredMixin, UpdateView):
    model = Cliente
    template_name = 'cliente/editar_cliente.html'
    success_url = reverse_lazy("clientes:detalle_cliente")
    form_class = ClienteForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Edición de clientes'
        context['url_anterior'] = '/clientes/detalle_cliente'

        return context


class EliminarCliente(LoginRequiredMixin, DeleteView):
    model = Cliente
    template_name = 'cliente/eliminar_cliente.html'
    success_url = reverse_lazy("clientes:detalle_cliente")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Eliminar cliente'
        context['url_anterior'] = '/clientes/detalle_cliente'
        context['listar_url'] = '/clientes/detalle_cliente'

        return context
