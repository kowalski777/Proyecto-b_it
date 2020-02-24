from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50)
    email=models.EmailField()
    documento=models.IntegerField()
    departamento=models.CharField(max_length=50)
    ciudad=models.CharField(max_length=50)
    telefono=models.CharField(max_length=9)
    fecha_de_nacimiento=models.DateField()

class Articulo(models.Model):
    nombre=models.CharField(max_length=30)
    marca=models.CharField(max_length=30)
    categoria=models.CharField(max_length=30)
    precio=models.IntegerField()

class Pedido(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()
