# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('-created_at',)




class Store(BaseModel):
    nombre=models.CharField(max_length=500)
    logo=models.ImageField(null=True)
    correo=models.EmailField()
    telefono=models.CharField(max_length=20)
    facebook=models.URLField(null=True)
    twitter=models.URLField(null=True)
    direccion=models.CharField(max_length=500)
    latitud=models.DecimalField(max_digits=20, decimal_places=16)
    longitud=models.DecimalField(max_digits=20, decimal_places=16)

    def __str__(self):
        return self.nombre
class Sale(BaseModel):
    encabazado=models.CharField(max_length=5000)
    fecha_inicio=models.DateTimeField()
    fecha_fin=models.DateTimeField()
    foto=models.ImageField(null=True)
    descripcion=models.TextField(null=True)
    tienda=models.ForeignKey(Store)

    def __str__(self):
        return self.encabazado
# class SaleStore(BaseModel):
#     descripcion=models.TextField()
#     encabazado = models.CharField(max_length=500)
#     fecha_inicio = models.DateTimeField()
#     fecha_fin = models.DateTimeField()
#     nombreTienda=models.ForeignKey(Store, on_delete=models.CASCADE)
#     latitud=
#     longitud=
#     foto=
