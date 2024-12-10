from django.db import models

class NotaFiscal(models.Model):
    numero = models.CharField(max_length=20, unique=True)
    data_emissao = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Nota Fiscal {self.numero}"