from django.shortcuts import render
from .models import Componentes
# Create your views here.

def componentes(request):
    componentes = Componentes.objects.all()
    return render(request, 'componentes/componentes.html', {'Componentes': componentes})
