from django.shortcuts import render
#importa todas as tabelas
from .models import *
from .models import Banner

# Create your views here.
def homepage(request):
    #a buscar os banners ativos no banco de dados e adicioná-los ao contexto da view homepage.
    banners = Banner.objects.filter(ativo=True)
    context = {'banners': banners}
    return render(request, 'homepage.html', context)


def loja(request, nome_categoria=None):
  #codigo para exibir os dados da tabela no html
  produtos = Produto.objects.filter(ativo=True)  # Consulta todos os produtos
  context = {"produtos": produtos}
  return render(request, 'loja.html', context)


def carrinho(request):
  return render(request, 'carrinho.html')

def checkout(request):
  return render(request, 'checkout.html')

def minha_conta(request):
  return render(request, 'usuario/minhaconta.html')

def login(request):
  return render(request, 'usuario/login.html')