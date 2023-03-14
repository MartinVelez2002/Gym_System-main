import json

from django.db import transaction
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import *
from modulos.finanzas.models import *
from modulos.finanzas.forms import *
from modulos.mensualidad.models import *
from modulos.maquinaria.models import *
from modulos.instrumentos.models import *
from django.contrib.auth.mixins import LoginRequiredMixin

class DetalleFinanzas(LoginRequiredMixin, ListView):
    template_name = 'finanzas/detalle_finanzas.html'
    context_object_name = 'Finanzs'
    model = Finanzas
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get("query")
        print(query)
        if query:
            return self.model.objects.filter(anio__icontains=query) \
                or self.model.objects.filter(mes__icontains=query)
        else:
            return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Registro de Finanzas'

        return context


class RellenarFinanza(LoginRequiredMixin, CreateView):
    model = Finanzas
    template_name = 'finanzas/añadir_registro_finanzas.html'
    form_class = FormFinanzas
    success_url = reverse_lazy("finanzas:detalle_finanzas")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Añadir Registro de Finanzas'
        context['action_save'] = self.request.path
        context['url_anterior'] = '/finanzas/detalle_finanzas/'
        context['fecha'] = self.request.GET.get("fecha") or ""
        context['mensualidades'] = json.dumps(self.Mensualidad_dict())
        context['maquinaria'] = json.dumps(self.Maquinaria_dict())
        context['instrumento'] = json.dumps(self.Instrumento_dict())
        context['action'] = "add"
        # bandera para validar una agregación de registro
        return context

    def Mensualidad_dict(self):
        listado = []
        mensu = Mensualidad.objects.all()

        for i in mensu:
            items = {}
            items['cliente'] = str(i.cliente)
            items['precio'] = str(i.precio)
            items['fecha_inicio'] = str(i.fecha_inicio)
            items['fecha_finalizacion'] = str(i.fecha_finalizacion)

            listado.append(items)

        return listado

    def Maquinaria_dict(self):
        listado = []
        maquina = Maquinaria.objects.all()

        for i in maquina:
            items = {}
            items['Cantidad'] = str(i.Cantidad)
            items['precio'] = str(i.precio_maquinaria)
            items['fecha'] = str(i.fecha_compra_maquinaria)

            listado.append(items)

        return listado

    def Instrumento_dict(self):
        listado = []
        instru = Instrumento.objects.all()

        for i in instru:
            items = {}
            items['Cantidad'] = str(i.cantidad)
            items['precio'] = str(i.precio_instrumento)
            items['fecha'] = str(i.fecha_compra_instrumento)

            listado.append(items)

        return listado

    def post(self, request, *args, **kwargs):
        resp = {}
        try:
            data = json.loads(request.body)
            if data['action'] == 'add':

                with transaction.atomic():
                    registro_finanzas = Finanzas()
                    registro_finanzas.anio = data['anio']
                    registro_finanzas.mes = data['mes']
                    registro_finanzas.mensualidades = int(data['mensualidades'])
                    registro_finanzas.ingresos = float(data['ingresos'])
                    registro_finanzas.gastos = float(data['gastos'])
                    registro_finanzas.ganancias = float(data['ganancias'])
                    registro_finanzas.save()
                    print("hola")
                    resp["grabar"] = "ok"
            else:
                pass
        except Exception as e:
            resp["grabar"] = str(e)
            print(e)

        return JsonResponse(resp, safe="false")


class EditarFinanzas(LoginRequiredMixin, UpdateView):
    model = Finanzas
    template_name = 'finanzas/editar_registro_finanzas.html'
    success_url = reverse_lazy("clientes:detalle_cliente")
    form_class = FormFinanzas

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = f"/finanzas/editar_finanzas/{self.get_object().id}"
        context['titulo'] = 'Edición de Finanzas'
        context['url_anterior'] = '/finanzas/detalle_finanzas'
        context['mensualidades'] = json.dumps(self.Mensualidad_dict())
        context['maquinaria'] = json.dumps(self.Maquinaria_dict())
        context['instrumento'] = json.dumps(self.Instrumento_dict())
        context['detalle_finanzas'] = json.dumps(self.get_detalleFinanzas())
        context['action'] = 'edit'
        return context

    def Mensualidad_dict(self):
        listado = []
        mensu = Mensualidad.objects.all()

        for i in mensu:
            items = {}
            items['cliente'] = str(i.cliente)
            items['precio'] = str(i.precio)
            items['fecha_inicio'] = str(i.fecha_inicio)
            items['fecha_finalizacion'] = str(i.fecha_finalizacion)

            listado.append(items)

        return listado

    def Maquinaria_dict(self):
        listado = []
        maquina = Maquinaria.objects.all()

        for i in maquina:
            items = {}
            items['Cantidad'] = str(i.Cantidad)
            items['precio'] = str(i.precio_maquinaria)
            items['fecha'] = str(i.fecha_compra_maquinaria)

            listado.append(items)

        return listado

    def Instrumento_dict(self):
        listado = []
        instru = Instrumento.objects.all()

        for i in instru:
            items = {}
            items['Cantidad'] = str(i.cantidad)
            items['precio'] = str(i.precio_instrumento)
            items['fecha'] = str(i.fecha_compra_instrumento)

            listado.append(items)

        return listado

    def post(self, request, *args, **kwargs):
        resp = {}
        try:
            data = json.loads(request.body)
            if data['action'] == 'edit':
                with transaction.atomic():
                    registro_finanzas = self.get_object()
                    print(registro_finanzas)
                    registro_finanzas.anio = data['anio']
                    registro_finanzas.mes = data['mes']
                    registro_finanzas.mensualidades = int(data['mensualidades'])
                    registro_finanzas.ingresos = float(data['ingresos'])
                    registro_finanzas.gastos = float(data['gastos'])
                    registro_finanzas.ganancias = float(data['ganancias'])
                    registro_finanzas.save()
                    resp["grabar"] = "ok"

            else:
                pass
        except Exception as e:
            resp["grabar"] = str(e)
            print(e)

        return JsonResponse(resp, safe="false")

    def get_detalleFinanzas(self):
        detalle = Finanzas.objects.filter(id=self.get_object().id).values()[0]
        items = {}
        items['anio'] = detalle["anio"]
        items['mes'] = detalle["mes"]
        items['mensualidades'] = str(detalle["mensualidades"])
        items['ingresos'] = str(detalle["ingresos"])
        items['gastos'] = str(detalle["gastos"])
        items['ganancias'] = str(detalle["ganancias"])
        print(items)
        return detalle


class EliminarFinanzas(LoginRequiredMixin, DeleteView):
    model = Finanzas
    template_name = 'finanzas/eliminar_registro_finanzas.html'
    success_url = reverse_lazy("finanzas:detalle_finanzas")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Eliminar Registro de Finanzas'
        context['url_anterior'] = '/finanzas/detalle_finanzas'
        context['listar_url'] = '/finanzas/detalle_finanzas'

        return context
