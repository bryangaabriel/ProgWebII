# advogados/models.py
from django.db import models

class Advogado(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(default="example@email.com")  # Valor padrão para email
    telefone = models.CharField(max_length=15, default="00000000000")  # Valor padrão para telefone
    oab = models.CharField(max_length=15)
    especializacao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
