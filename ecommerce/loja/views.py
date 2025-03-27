from django.shortcuts import render
#importa todas as tabelas
from .models import *

# Create your views here.
def homepage(request):
  return render(request, 'homepage.html')

def loja(request):
  #codigo para exibir os dados da tabela no html
  produtos = Produto.objects.all()  # Consulta todos os produtos
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