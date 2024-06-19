from django.urls import path
from . import views

urlpatterns =[
    path('', views.hello),
    path('index/', views.index),
    path('carrito/', views.carrito),
    path('productos/', views.productos),
    path('contacto/', views.contacto),
    path('admin/', views.admin),

]