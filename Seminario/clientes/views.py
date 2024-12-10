from django.shortcuts import render
from .models import Cliente

def index(request):
    clientes = Cliente.objects.all()  # Pega todos os clientes
    return render(request, 'clientes/clientes.html', {'clientes': clientes})
