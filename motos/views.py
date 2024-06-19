from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("wema xixetu")

def index(request):
    return render(request, 'index.html')

def carrito(request):
    return render(request, 'carrito.html')

def productos(request):
    return render(request, 'productos.html')

def contacto(request):
    return render(request, 'contacto.html')

def admin(request):
    return render(request, 'admin.html')