from django.http import HttpResponse
from django.shortcuts import render, redirect
from motos.carrito import Carrito
from motos.models import Producto

def hello(request):
    return HttpResponse("wema xixetu")

def index(request):
    return render(request, 'index.html')

def tienda(request):
    productos = Producto.objects.all()
    return render(request, 'tienda.html', {'productos':productos})

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("Tienda")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("Tienda")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("Tienda")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("Tienda")




def productos(request):
    return render(request, 'productos.html')

def contacto(request):
    return render(request, 'contacto.html')

def admin(request):
    return render(request, 'admin.html')