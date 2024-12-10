# advogados/admin.py
from django.contrib import admin
from .models import Advogado

class AdvogadoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'oab', 'especializacao', 'email', 'telefone')  # Corrigido para 'oab'

admin.site.register(Advogado, AdvogadoAdmin)
