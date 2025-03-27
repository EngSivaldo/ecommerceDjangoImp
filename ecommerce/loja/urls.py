from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name='homepage'),
    path('homepage/', homepage, name='homepage'),
    path('loja/', loja, name='loja'),
    path('minhaconta/', minha_conta, name='minhaconta'),
    path('login/', login, name='login'),
    path('carrinho/', carrinho, name='carrinho'),
    path('checkout/', checkout, name='checkout'),
]
#depois disso criar funcoes na views