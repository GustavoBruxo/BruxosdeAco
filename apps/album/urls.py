from django.urls import path
from .views import *

urlpatterns = [
    path('', albuns, name='albuns'),
    path('album/<int:id_album>', album, name='album'),
    path('cria/album', cria_album, name='cria_album'),
    path('edita/<int:id_album>', edita_album, name='edita_album'),
    path('deleta/<int:id_album>', deleta_album, name='deleta_album'),
    path('atualiza_album', atualiza_album, name='atualiza_album')
]
