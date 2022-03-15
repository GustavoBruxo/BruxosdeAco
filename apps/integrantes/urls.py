from django.urls import path
from .views import *

urlpatterns = [
    path('', integrantes, name='integrantes'),
    path('cria/integrante', cria_integrante, name='cria_integrante'),
    path('memorial', memorial, name='memorial'),
    path('edita/<int:id_integrante>', edita_integrante, name='edita_integrante'),
    path('deleta/<int:id_integrante>', deleta_integrante, name='deleta_integrante'),
    path('atualiza_integrante', atualiza_integrante, name='atualiza_integrante')
]
