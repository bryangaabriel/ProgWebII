from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15, blank=True)
    endereco = models.TextField()
    cpf = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return self.nome