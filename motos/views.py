from django.http import HttpResponse
from django.shortcuts import render, redirect
from motos.carrito import Carrito
from motos.models import *


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
    usuariosListado = Usuarios.objects.all()
    return render(request, 'admin.html', {"usuarios": usuariosListado})

def registrarUsuario(request):
    usuario=request.POST['username']
    nombre=request.POST['name']
    email=request.POST['email']
    password=request.POST['password']

    usuarios = Usuarios.objects.create(
        usuario=usuario, nombre=nombre, email=email, password=password)
    return redirect('/admini#user')

def eliminarUsuario(request, usuario):
    user = Usuarios.objects.get(usuario=usuario)
    user.delete()

    return redirect('/admini#user')

# Carrusel

def HomeView(request):
    carousel = Carousel.objects.all()
    context  = {
        'carousel' : carousel
    }
    return render(request, "index.html", context)