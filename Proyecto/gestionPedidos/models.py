from django.db import models

# Create your models here.

class Cliente(models.Model):
    documento_cliente=models.IntegerField()
    nombre_cliente=models.CharField(max_length=30)
    apellido_cliente=models.CharField(max_length=30)
    email_cliente=models.EmailField()
    direccion_cliente=models.CharField(max_length=50)
    depar_cliente=models.CharField(max_length=50)
    ciudad_cliente=models.CharField(max_length=50)
    telefono_cliente=models.CharField(max_length=9)
    fechaNac_cliente=models.DateField()
    rut_cliente=models.IntegerField()

class Articulo(models.Model):
    id_articulo=models.CharField(max_length=30)
    nombre_articulo=models.CharField(max_length=30)
    marca_articulo=models.CharField(max_length=30)
    categoria_articulo=models.CharField(max_length=30)
    precio_articulo=models.IntegerField()

class Pedido(models.Model):
    id_pedido=models.IntegerField()
    documento_cliente=models.IntegerField()
    fecha_pedido=models.DateField()
    envio_pedido=models.BooleanField()


class Detalle(models.Model):
    num_detalle =models.IntegerField()
    id_articulo =models.IntegerField()
    cantidad_detalle =models.IntegerField()
    precio_detalle =models.IntegerField()
   
