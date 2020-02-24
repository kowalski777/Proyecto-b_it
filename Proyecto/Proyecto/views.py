from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def inicio_sesion(request):
    return render(request, "inicio_sesion.html")

def registro(request):
    return render(request, "registro.html")

def carrito(request):
    return render(request, "carrito.html")

def busqueda_producto(request):
    return render(request, "busqueda_producto.html")

