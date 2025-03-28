from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
#importa todas as tabelas
from .models import *
from .models import Banner
from .models import ItemEstoque


# Create your views here.
def homepage(request):
    #a buscar os banners ativos no banco de dados e adicioná-los ao contexto da view homepage.
    banners = Banner.objects.filter(ativo=True)
    context = {'banners': banners}
    return render(request, 'homepage.html', context)

def loja(request, nome_categoria=None):
    produtos = Produto.objects.filter(ativo=True)  # Consulta todos os produtos ativos
    if nome_categoria:
        produtos = produtos.filter(categoria__nome=nome_categoria)  # Filtra os produtos pela categoria
    context = {"produtos": produtos}
    return render(request, 'loja.html', context)

#funcao para ver produto(criar ver_produto.html)
def ver_produto(request, id_produto):
    produto = Produto.objects.get(id=id_produto)
    # Verifica se a quantidade de itens em estoque é maior que zero (quantidade__gt=0)
    itens_estoque = ItemEstoque.objects.filter(produto=produto, quantidade__gt=0)
    if len(itens_estoque) > 0:
        tem_estoque = True
        cores = {item.cor for item in itens_estoque}
    else:
        tem_estoque = False
        cores = {}
    context = {"produto": produto, "itens_estoque": itens_estoque, "tem_estoque": tem_estoque, "cores": cores}
    return render(request, "ver_produto.html", context)

# def ver_produto(request, id_produto):
#     produto = get_object_or_404(Produto, id=id_produto)
#     item_estoque = ItemEstoque.objects.filter(produto=produto, quantidade__gt=0).first()
#     context = {
#         'item_estoque': item_estoque,
#     }
#     return render(request, 'ver_produto.html', context)


def carrinho(request):
  return render(request, 'carrinho.html')

def checkout(request):
  return render(request, 'checkout.html')

def minha_conta(request):
  return render(request, 'usuario/minhaconta.html')

def login(request):
  return render(request, 'usuario/login.html')