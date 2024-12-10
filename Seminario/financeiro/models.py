from django.db import models
from clientes.models import Cliente

class Pagamento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_pagamento = models.DateField()
    descricao = models.TextField()

    def __str__(self):
        return f"{self.cliente.nome} - R$ {self.valor}"
