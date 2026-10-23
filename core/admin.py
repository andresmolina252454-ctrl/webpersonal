from django.contrib import admin
from .models import Persona

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('nombres', 'apellidos', 'titulo_academico', 'correo_electronico')