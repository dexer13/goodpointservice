# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
import json
import math
from decimal import Decimal

from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView, CreateView
from django.views.generic.base import View
from rest_framework.viewsets import ViewSet, ModelViewSet

from stores.forms import StoreForm, SaleForm
from stores.models import Store, Sale
from stores.serializers import StoreSerializer


class StoreView(CreateView):
    template_name= 'store.html'
    form_class = StoreForm
    success_url = reverse_lazy('create_store')
    def form_valid(self, form):
        super(StoreView, self).form_valid(form)
        messages.success(request=self.request, message='La tienda se ha registrado correctamente.')
        return HttpResponseRedirect(self.get_success_url())

class SaleView(CreateView):
    template_name= 'sale.html'
    form_class = SaleForm
    success_url = reverse_lazy('create_sale')
    def form_valid(self, form):
        super(SaleView, self).form_valid(form)
        messages.success(request=self.request, message='La promoción ha sido registrada correctamente.')
        return HttpResponseRedirect(self.get_success_url())

class StoreViewSet(ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

class SuperpromocionesView(View):
    distance=0.0075

    def get(self, *args, **kwargs):
        latitud=Decimal(self.request.GET['latitud'])
        longitud=Decimal(self.request.GET['longitud'])
        sales=Sale.objects.all()
        superpromocion=list()
        for s in sales:
            distancia= math.sqrt(math.pow(latitud - s.tienda.latitud, 2)+math.pow(longitud-s.tienda.longitud, 2))
            if distancia<self.distance:
                # crear json superpromoción
                from django.utils import timezone
                now = timezone.now()
                if s.fecha_inicio < now and now < s.fecha_fin:
                    superpromocion.append({
                        'id':s.id,
                        'descripcion':s.descripcion,
                        'encabezado':s.encabazado,
                        'fecha_inicio':s.fecha_inicio,
                        'fecha_fin':s.fecha_fin,
                        'latitud':float(s.tienda.latitud),
                        'longitud':float(s.tienda.longitud),
                        'nombretienda':s.tienda.nombre,
                        'foto':s.foto.url,
                    })
        dumps=json.dumps(superpromocion, default=myconverter)
        return HttpResponse(dumps)

def decimal_default(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError

def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()
    return o