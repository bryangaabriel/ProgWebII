from rest_framework import viewsets
from django.shortcuts import render
from .models import Documento
from .serializers import DocumentoSerializer

# ViewSet para a API
class DocumentoViewSet(viewsets.ModelViewSet):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer

# View para renderizar o template HTML
def documentos(request):
    return render(request, 'documentos/documentos.html')  # Garante o caminho correto para o template