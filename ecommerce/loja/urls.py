from django.urls import path
#importar tudo da views( ex: homepage)
from.views import *

urlpatterns = [
    path('', homepage, name='homepage'),

]
