from django.shortcuts import render, redirect
from JRComponentes.models import Componentes
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from JRApp.forms import RegisterForm
from django.contrib.auth import logout

def index(request):
    componentes = Componentes.objects.all()
    return render(request, 'JR_SISTEMAS/index.html', {'Componentes': componentes})

def login(request):
    return render(request,'login.html')

def exit(request):
    logout(request)
    return redirect('index')

def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request,'registration/registration.html',{'form':RegisterForm(data=request.POST)})

def product_register(request):
    return render(request, 'JR_SISTEMAS/product_register.html')

"""

def user_register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('success')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
"""