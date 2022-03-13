from django.contrib import admin
from .models import Banner


class ListandoBanneres(admin.ModelAdmin):
    list_display = ('id', 'banner', 'banner_ativo')
    list_display_links = ('id', 'banner')
    list_editable = ('banner_ativo',)
    list_per_page = 10


admin.site.register(Banner, ListandoBanneres)
