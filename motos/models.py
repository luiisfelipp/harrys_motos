from django.db import models

# Create your models here.
class Producto(models.Model):
    modelo = models.CharField(max_length=100)
    cilindrada = models.CharField(max_length=100)
    precio = models.IntegerField()
    imagen = models.ImageField(null = True)

    def __str__(self):
        return f'{self.modelo} -> {self.precio}'

class Usuarios(models.Model):
    usuario = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.usuario} -> {self.email}'
    