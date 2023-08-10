from django.db import models

import os

def cliente_foto_directory(instance, filename):
    # Extrae el nombre del cliente y la extensión del archivo de imagen
    nombre_cliente, extension = os.path.splitext(filename)
    # Construye la ruta para guardar la imagen en la carpeta del cliente
    return f'clientes/{instance.nombre}/{nombre_cliente}{extension}'

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    foto = models.ImageField(upload_to=cliente_foto_directory, blank=True, null=True)

    def __str__(self):
        return self.nombre
