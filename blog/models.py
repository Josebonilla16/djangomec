from django.db import models
from django.utils import timezone

class Cliente(models.Model):
    nit = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=200)

class Servicio(models.Model):
    tipo = models.CharField(max_length=200)
    comentario = models.TextField()
    precio = models.CharField(max_length=200)

class Carro(models.Model):
    placa = models.CharField(max_length=200)
    marca = models.CharField(max_length=200)
    linea = models.CharField(max_length=200)
    modelo = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
