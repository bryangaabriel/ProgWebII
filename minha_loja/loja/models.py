from django.db import models

from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.PositiveIntegerField()
    categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15, blank=True)
    endereco = models.TextField()
    cpf = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return self.nome

class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=15, blank=True)
    endereco = models.TextField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15, blank=True)
    cargo = models.CharField(max_length=50)
    salario = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nome

class NotaFiscal(models.Model):
    numero = models.CharField(max_length=20, unique=True)
    data_emissao = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produtos = models.ManyToManyField(Produto, through='ProdutoNotaFiscal')
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Nota Fiscal {self.numero}"

class ProdutoNotaFiscal(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    nota_fiscal = models.ForeignKey(NotaFiscal, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantidade} x {self.produto.nome}"
