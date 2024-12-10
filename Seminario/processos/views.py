# processos/views.py
from django.shortcuts import render

def processos(request):
    return render(request, 'processos/processos.html')
