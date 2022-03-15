from datetime import datetime

from django.shortcuts import render, get_object_or_404, redirect
from .models import Album, Imagens
from django.core.paginator import Paginator


def albuns(request):
    """Lista todos os albuns criados na base"""
    albuns = Album.objects.get_queryset().filter(exibir_album=True)
    paginator = Paginator(albuns, 12)
    page = request.GET.get('page')
    albuns_por_pagina = paginator.get_page(page)

    dados = {
        'albuns': albuns_por_pagina
    }
    return render(request, 'album/albuns.html', dados)


def album(request, id_album):
    """Exibe o album selecionado"""
    album = get_object_or_404(Album, pk=id_album)
    imagens = Imagens.objects.get_queryset().filter(id_album=album)
    dados = {
        'album': album,
        'imagens': imagens
    }
    return render(request, 'album/album.html', dados)


def cria_album(request):
    """Cria um album na base de dados"""
    if request.method == 'POST':
        nome_album = request.POST['nome_album']
        foto_capa_album = request.FILES['foto_capa_album']
        local_album = request.POST['local_album']
        data_album = request.POST['data_album']
        exibir_album = request.POST['exibir_album']
        album_destaque = request.POST['album_destaque']
        imagens = request.FILES.getlist('imagens')

        if exibir_album == 'on':
            exibir_album = True

        if album_destaque == 'on':
            album_destaque = True

        album = Album.objects.create(nome_album=nome_album, local_album=local_album,
                                     foto_capa_album=foto_capa_album, data_album=data_album,
                                     exibir_album=exibir_album, album_destaque=album_destaque)
        album.save()
        id_album = get_object_or_404(Album, pk=album.pk)
        for img in imagens:
            imagem = Imagens.objects.create(imagem=img, id_album=id_album)
            imagem.save()

        return redirect('albuns')
    else:
        return render(request, 'album/cria_album.html')


def deleta_album(request, id_album):
    """Delete um album da base de dados"""
    album = get_object_or_404(Album, pk=id_album)
    album.delete()
    return redirect('albuns')


def edita_album(request, id_album):
    """Edita o album selecionado"""
    album = get_object_or_404(Album, pk=id_album)
    imagens = Imagens.objects.get_queryset().filter(id_album=album)

    data = album.data_album
    album.data_album = datetime.strftime(data, '%Y-%m-%d')

    dados = {
        'album': album,
        'imagens': imagens
    }
    return render(request, 'album/edita_album.html', dados)


def atualiza_album(request):
    if request.method == 'POST':
        id_album = request.POST['album.id']
        a = Album.objects.get(pk=id_album)
        a.nome_album = request.POST['nome_album']
        a.local_album = request.POST['local_album']
        a.data_album = request.POST['data_album']
        a.exibir_album = request.POST['exibir_album']
        a.album_destaque = request.POST['album_destaque']

        if 'foto_capa_album' in request.FILES:
            a.foto_capa_album = request.FILES['foto_capa_album']
        imagens = request.FILES.getlist('imagens')

        if a.exibir_album == 'on':
            a.exibir_album = True

        if a.album_destaque == 'on':
            a.album_destaque = True

        for img in imagens:
            imagem = Imagens.objects.create(imagem=img, id_album=id_album)
            imagem.save()
        a.save()
        return redirect('albuns')
