from django.contrib import admin
from .models import Integrantes, InMemorian

# Register your models here.


class ListandoIntegrantes(admin.ModelAdmin):
    list_display = ('id', 'nome_integrante', 'data_entrada',
                    'integrante_ativo', 'cargo_integrante')
    list_display_links = ('id', 'nome_integrante')
    search_fields = ('cargo_integrante',)
    list_editable = ('integrante_ativo', )
    list_per_page = 10


admin.site.register(Integrantes, ListandoIntegrantes)


class ListandoMemorial(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')
    list_per_page = 10


admin.site.register(InMemorian, ListandoMemorial)
