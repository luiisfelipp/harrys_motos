from django.urls import path
from . import views

urlpatterns =[
    path('', views.index),
    path('index/', views.index),
    path('carrito/', views.tienda, name='Tienda'),
    path('productos/', views.productos),
    path('contacto/', views.contacto),
    path('admin/', views.admin),
    path('agregar/<int:producto_id>/', views.agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', views.restar_producto, name="Sub"),
    path('limpiar/', views.limpiar_carrito, name="CLS"),
    
]
