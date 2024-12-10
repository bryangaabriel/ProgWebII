# advogados/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Advogado
from .forms import AdvogadoForm

# Lista de advogados
def listar_advogados(request):
    advogados = Advogado.objects.all()
    return render(request, 'listar_advogados.html', {'advogados': advogados})

# Adicionar advogado
def adicionar_advogado(request):
    if request.method == 'POST':
        form = AdvogadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_advogados')
    else:
        form = AdvogadoForm()
    return render(request, 'adicionar_advogado.html', {'form': form})

# Editar advogado
def editar_advogado(request, pk):
    advogado = get_object_or_404(Advogado, pk=pk)
    if request.method == 'POST':
        form = AdvogadoForm(request.POST, instance=advogado)
        if form.is_valid():
            form.save()
            return redirect('listar_advogados')
    else:
        form = AdvogadoForm(instance=advogado)
    return render(request, 'editar_advogado.html', {'form': form})

# Excluir advogado
def excluir_advogado(request, pk):
    advogado = get_object_or_404(Advogado, pk=pk)
    advogado.delete()
    return redirect('listar_advogados')

from rest_framework import viewsets
from .models import Advogado
from .serializers import AdvogadoSerializer

class AdvogadoViewSet(viewsets.ModelViewSet):
    queryset = Advogado.objects.all()
    serializer_class = AdvogadoSerializer
