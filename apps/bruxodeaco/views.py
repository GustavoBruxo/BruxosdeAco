from django.shortcuts import render
from .models import Banner
from album.models import Album
from django.core.paginator import Paginator


def index(request):
    banner = Banner.objects.filter(banner_ativo=True)
    albuns = Album.objects.filter(album_destaque=True)
    paginator = Paginator(albuns, 6)
    page = request.GET.get('page')
    albuns_por_pagina = paginator.get_page(page)

    dados = {
        'banner': banner,
        'albuns': albuns_por_pagina
    }
    return render(request, 'bruxodeaco/index.html', dados)


def cadastros(request):
    return render(request, 'bruxodeaco/cadastros.html')
