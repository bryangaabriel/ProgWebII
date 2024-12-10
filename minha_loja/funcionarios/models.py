from django.db import models

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15, blank=True)
    cargo = models.CharField(max_length=50)
    salario = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nome