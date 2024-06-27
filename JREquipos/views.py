from django.shortcuts import render
from .models import Equipo
# Create your views here.

def equipos(request):
    equipo = Equipo.objects.all()
    return render(request, 'equipos/equipos.html', {'Equipo': equipo})
