from django.db import models

class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=15, blank=True)
    endereco = models.TextField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome