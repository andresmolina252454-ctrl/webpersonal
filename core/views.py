from django.shortcuts import render
from .models import Persona

def home(request):
    persona = Persona.objects.first()
    return render(request, "core/home.html", {'persona': persona})

def about(request):
    persona = Persona.objects.first()
    return render(request, "core/about.html", {'persona': persona})

def contact(request):
    persona = Persona.objects.first()
    return render(request, "core/contact.html", {'persona': persona})