from django.db import models
import datetime

class Documento(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)
    arquivo = models.FileField(upload_to='documentos/')
    criado_em = models.DateTimeField(auto_now_add=True)
    data_inicio = models.DateTimeField(default=datetime.datetime.now)  # Campo não nulo com valor padrão

    def __str__(self):
        return self.titulo
