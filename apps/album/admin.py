from django.contrib import admin
from .models import Album, Imagens

# Register your models here.


class ListandoAlbuns(admin.ModelAdmin):
    list_display = ('id', 'nome_album', 'local_album',
                    'data_album', 'exibir_album', 'album_destaque')
    list_display_links = ('id', 'nome_album')
    search_fields = ('nome_album', 'loca_album')
    list_editable = ('exibir_album', 'album_destaque')
    list_per_page = 20


admin.site.register(Album, ListandoAlbuns)


class ListandoImagens(admin.ModelAdmin):
    list_display = ('id', 'id_album', 'imagem')
    list_display_links = ('id', 'imagem')
    list_per_page = 20


admin.site.register(Imagens, ListandoImagens)
