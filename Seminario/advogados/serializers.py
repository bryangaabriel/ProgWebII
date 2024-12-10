# advogados/serializers.py
from rest_framework import serializers
from .models import Advogado

class AdvogadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advogado
        fields = ['id', 'nome', 'oab', 'especializacao']  # Remove 'email' from here if it's not in the model
