from django.urls import path, re_path
from . import views, views_login

urlpatterns =[
    path('', views.HomeView),
    path('carrito/', views.tienda, name='Tienda'),
    path('productos/', views.productos),
    path('contacto/', views.contacto),
    path('admini/', views.admin),
    path('agregar/<int:producto_id>/', views.agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', views.restar_producto, name="Sub"),
    path('limpiar/', views.limpiar_carrito, name="CLS"),
    path('registrarUsuario/', views.registrarUsuario),
    path('admini/eliminarUsuario/<str:usuario>', views.eliminarUsuario),
    re_path('login', views_login.login),
    re_path('register', views_login.register),
    re_path('profile', views_login.profile), 
    path('index/', views.HomeView),
    
]
