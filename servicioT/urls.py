from django.urls import path
from servicioT import views

urlpatterns= [
    path('', views.servicioT, name='servicioT'),
]

