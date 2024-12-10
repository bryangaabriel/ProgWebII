from django.db import models
from clientes.models import Cliente

class Processo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    descricao = models.TextField()
    status = models.CharField(max_length=20, choices=[
        ('aberto', 'Aberto'),
        ('em andamento', 'Em Andamento'),
        ('concluído', 'Concluído')
    ])
    data_inicio = models.DateField()

    def __str__(self):
        return f"{self.cliente.nome} - {self.status}"
