from django.shortcuts import render

# Função index para renderizar o template
def index(request):
    return render(request, 'financeiro/financeiro.html')
