
from advogados.models import Advogado
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')




def list_advogados(request):
    advogados = Advogado.objects.all()
    return render(request, 'advogados/listar_advogados.html', {'advogados': advogados})