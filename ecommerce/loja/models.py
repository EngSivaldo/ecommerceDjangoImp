from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    nome = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    telefone = models.CharField(max_length=200, null=True, blank=True)
    id_sessao = models.CharField(max_length=200, null=True, blank=True)
    usuario = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    
     #faz aparecer o nome dessa categoria no banco dados
    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nome

class Tipo(models.Model):
    nome = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    imagem = models.CharField(max_length=400, null=True, blank=True)
    nome = models.CharField(max_length=200, null=True, blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    ativo = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.SET_NULL)
    tipo = models.ForeignKey(Tipo, null=True, blank=True, on_delete=models.SET_NULL)

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
    rua = models.CharField(max_length=400, null=True, blank=True)
    numero = models.IntegerField(default=0)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    cep = models.CharField(max_length=400, null=True, blank=True)
    cidade = models.CharField(max_length=400, null=True, blank=True)
    estado = models.CharField(max_length=400, null=True, blank=True)
    cliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.rua}, {self.numero} - {self.cidade}/{self.estado}'

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.SET_NULL)
    finalizado = models.BooleanField(default=False)
    codigo_transacao = models.CharField(max_length=200, null=True, blank=True)
    endereco = models.ForeignKey(Endereco, null=True, blank=True, on_delete=models.SET_NULL)
    data_finalizacao = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'Pedido {self.id} - {self.cliente.nome}'

class ItensPedido(models.Model):
    itemestoque = models.ForeignKey(ItemEstoque, null=True, blank=True, on_delete=models.SET_NULL)
    quantidade = models.IntegerField(default=0)
    pedido = models.ForeignKey(Pedido, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.itemestoque.produto.nome} - {self.itemestoque.cor} - {self.itemestoque.tamanho} - {self.quantidade}'
    


    #sempre que fizer alguma alteracao nas tabelas executar comandos no terminal
    # python manage.py makemigrations
    # python manage.py migrate  
    # python manage.py runserver   

#Criar um super user

#python manage.py createsuperuser

#sivaldo@gmail.com

#Criar um super user

#python manage.py createsuperuser

#sivaldo@gmail.com
#senha 123

#adicionar as tabelas no admin
#from .models import *

# Register your models here.
# admin.site.register(Cliente)