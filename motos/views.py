from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("wema xixetu")

def index(request):
    return render(request, 'index.html')