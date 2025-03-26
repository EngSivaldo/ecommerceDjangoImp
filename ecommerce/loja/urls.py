from django.urls import path
#importar tudo da views( ex: homepage)
from.views import *

urlpatterns = [
    path('', homepage, name='homepage'),
    path('loja/', loja, name='homepage'),
    path('minhaconta/', minha_conta, name='minha_conta'),
    path('login', login, name='login'),
    path('carrinho', carrinho, name='carrinho'),
    path('checkout', checkout, name='checkout'),

]


#depois disso criar funcoes na views