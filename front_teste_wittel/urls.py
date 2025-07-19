from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.clientes, name='clientes'),
    path('clientes/', views.clientes, name='clientes'),
    path('cadastrar_cliente/', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('relatorios/', views.relatorios, name='relatorios'),
]
