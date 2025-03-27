from django.db import models
#importar a tabela usuario do django
from django.contrib.auth.models import User


#Tabelas========================================
class Cliente(models.Model):
    nome = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    telefone = models.CharField(max_length=200, null=True, blank=True)
    #identifica o usuario
    id_sessao = models.CharField(max_length=200, null=True, blank=True)
    #tem relacao a tabela do django
    usuario = models.OneToOneField(User, null=True, blank=True,  on_delete=models.CASCADE)

    def __str__(self):
        return self.nome




class Categoria(models.Model): #(Masculino, Feminino, infantil)
    nome = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nome

class Tipo(models.Model): #(camisa, bermuda, calça)
    nome = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nome



class Produto(models.Model):
    imagem = models.CharField(max_length=400, null=True, blank=True)
    nome = models.CharField(max_length=200, null=True, blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    ativo = models.BooleanField(default=True)
    #associa a tabela categoria
    categoria = models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.SET_NULL)
    #associa a tabela tipo
    tipo = models.ForeignKey(Tipo, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nome



class ItemEstoque(models.Model):
    produto = models.ForeignKey(Produto, null=True, blank=True, on_delete=models.SET_NULL)
    cor = models.CharField(max_length=200, null=True, blank=True)
    tamanho = models.CharField(max_length=200, null=True, blank=True)
    quantidade = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.produto.nome} - {self.cor} - {self.tamanho}'


class Endereco(models.Model):
    rua = models.CharField(max_length=400,  null=True, blank=True, on_delete=models.SET_NULL)
    numero = models.IntegerField(default=0)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    cep = models.CharField(max_length=400,  null=True, blank=True)
    cidade = models.CharField(max_length=400,  null=True, blank=True)
    estado = models.CharField(max_length=400,  null=True, blank=True)
    cliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.rua}, {self.numero} - {self.cidade}/{self.estado}'


class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.SET_NULL)
    finalizado = models.BooleanField(default=False)
    codigo_transacao = models.CharField(max_length=200, null=True, blank=True)
    endereco = models.ForeignKey('Endereco',null=True, blank=True, on_delete=models.SET_NULL)
    data_finalizacao = models.DateTimeField(null=True, blank=True)
    # itenspedido = models.ManyToManyField(ItensPedido)

    def __str__(self):
        return f'Pedido {self.id} - {self.cliente.nome}'


class ItensPedido(models.Model):
    itemestoque = models.ForeignKey(ItemEstoque, null=True, blank=True, on_delete=models.SET_NULL)
    quantidade = models.IntegerField(default=0)
    pedido = models.ForeignKey(Pedido, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.itemestoque.produto.nome} - {self.itemestoque.cor} - {self.itemestoque.tamanho} - {self.quantidade}'


