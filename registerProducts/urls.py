from django.urls import path
from . import views

urlpatterns= [
    path('', views.product_register, name="products"),
]