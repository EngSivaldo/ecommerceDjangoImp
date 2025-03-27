from django.db import models
#importar a tabela usuario do django
from django.contrib.auth.models import User


#Tabelas========================================
class Cliente(models.Model):
    nome = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    telefone = models.CharField(max_length=100, null=True, blank=True)
    #identifica o usuario
    id_sessao = models.CharField(max_length=100, null=True, blank=True)
    #tem relacao a tabela do django
    usuario = models.OneToOneField(User, null=True, blank=True,  on_delete=models.CASCADE)

#     def __str__(self):
#         return self.nome




# class Categoria(models.Model): #(Masculino, Feminino, infantil)
#     nome = models.CharField(max_length=50)

#     def __str__(self):
#         return self.nome

# class Tipo(models.Model): #(camisa, bermuda, calça)
#     nome = models.CharField(max_length=50)

#     def __str__(self):
#         return self.nome



# class Produto(models.Model):
#     imagem = models.ImageField(upload_to='produtos/')
#     nome = models.CharField(max_length=100)
#     preco = models.DecimalField(max_digits=10, decimal_places=2)
#     ativo = models.BooleanField(default=True)
#     #associa a tabela categoria
#     categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
#       #associa a tabela tipo
#     tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.nome



# class ItemEstoque(models.Model):
#     produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
#     cor = models.CharField(max_length=50)
#     tamanho = models.CharField(max_length=5)
#     quantidade = models.IntegerField()

#     def __str__(self):
#         return f'{self.produto.nome} - {self.cor} - {self.tamanho}'

# class ItensPedido(models.Model):
#     itemestoque = models.ForeignKey(ItemEstoque, on_delete=models.CASCADE)
#     quantidade = models.IntegerField()

#     def __str__(self):
#         return f'{self.itemestoque.produto.nome} - {self.itemestoque.cor} - {self.itemestoque.tamanho} - {self.quantidade}'


# class Pedido(models.Model):
#     cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
#     data_finalizacao = models.DateTimeField()
#     finalizado = models.BooleanField(default=False)
#     id_transacao = models.CharField(max_length=100)
#     endereco = models.ForeignKey('Endereco', on_delete=models.CASCADE)
#     itenspedido = models.ManyToManyField(ItensPedido)

#     def __str__(self):
#         return f'Pedido {self.id} - {self.cliente.nome}'



# class Endereco(models.Model):
#     rua = models.CharField(max_length=100)
#     numero = models.CharField(max_length=10)
#     complemento = models.CharField(max_length=100, blank=True, null=True)
#     cep = models.CharField(max_length=10)
#     cidade = models.CharField(max_length=50)
#     estado = models.CharField(max_length=50)
#     cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

#     def __str__(self):
#         return f'{self.rua}, {self.numero} - {self.cidade}/{self.estado}'