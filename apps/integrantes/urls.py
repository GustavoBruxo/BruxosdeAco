from django.urls import path
from .views import *

urlpatterns = [
    path('', integrantes, name='integrantes'),
    path('cria/integrante', cria_integrante, name='cria_integrante'),
    path('memorial', memorial, name='memorial')
]
