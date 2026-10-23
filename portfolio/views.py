from django.shortcuts import render
from .models import Project
from core.models import Persona

def portfolio(request):
    projects = Project.objects.all()
    persona = Persona.objects.first()
    return render(request, "portfolio/portfolio.html", {'projects': projects, 'persona': persona})