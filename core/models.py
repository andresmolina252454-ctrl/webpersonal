from django.db import models

class Persona(models.Model):
    nombres = models.CharField(max_length=100, verbose_name="Nombres")
    apellidos = models.CharField(max_length=100, verbose_name="Apellidos")
    direccion = models.CharField(max_length=200, verbose_name="Dirección")
    telefono = models.CharField(max_length=20, verbose_name="Teléfono")
    titulo_academico = models.CharField(max_length=150, verbose_name="Título Académico")
    biografia = models.TextField(verbose_name="Biografía")
    correo_electronico = models.EmailField(verbose_name="Correo Electrónico")
    dedicacion = models.CharField(max_length=100, verbose_name="Dedicación Persona")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"