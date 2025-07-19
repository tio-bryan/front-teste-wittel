from django.shortcuts import render
from . import services
from django.http import HttpResponseRedirect
from .forms import ClienteForm


def clientes(request):
    clientes = services.get_clientes()

    return render(request, 'pages/clientes.html', { 'clientes': clientes })

def cadastrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')

    else:
        form = ClienteForm()

    return render(request, 'pages/cadastrar_cliente.html', { 'form': form })

def relatorios(request):
    return render(request, 'pages/relatorios.html')