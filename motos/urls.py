from django.urls import path
from . import views

urlpatterns =[
    path('', views.hello),
    path('index/', views.index),
    path('carrito/', views.carrito)

]