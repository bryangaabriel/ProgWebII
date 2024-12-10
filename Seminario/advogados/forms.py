# advogados/forms.py
from django import forms
from .models import Advogado

class AdvogadoForm(forms.ModelForm):
    class Meta:
        model = Advogado
        fields = ['nome', 'email', 'telefone', 'oab', 'especializacao']
