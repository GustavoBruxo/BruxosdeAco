from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from .models import Integrantes, InMemorian
from django.core.paginator import Paginator


def memorial(request):
    """Exibe todos as pessoas marcantes para o motoclube"""
    memorias = InMemorian.objects.all()
    paginator = Paginator(memorias, 12)
    page = request.GET.get('page')
    memorias_por_pagina = paginator.get_page(page)

    dados = {
        'memorias': memorias_por_pagina
    }
    return render(request, 'integrantes/memorial.html', dados)


def integrantes(request):
    """Exibe todos os integrantes do Motoclube"""
    integrantes_motoclube = Integrantes.objects.order_by('cargo_integrante')
    paginator = Paginator(integrantes_motoclube, 12)
    page = request.GET.get('page')
    integrantes_por_pagina = paginator.get_page(page)

    dados = {
        'integrantes': integrantes_por_pagina
    }
    return render(request, 'integrantes/integrantes.html', dados)


def cria_integrante(request):
    """Cria integrante"""
    if request.method == 'POST':
        nome_integrante = request.POST['nome_integrante']
        foto_integrante = request.FILES['foto_integrante']
        data_entrada = request.POST['data_entrada']
        integrante_ativo = request.POST['integrante_ativo']
        cargo_integrante = request.POST['cargo_integrante']

        # Valida integrante ativo
        if integrante_ativo == 'on':
            integrante_ativo = True
        else:
            integrante_ativo = False

        # Valida o cargo do integrante
        for id_cargo, nivel in Integrantes.NIVEL:
            if nivel == cargo_integrante:
                cargo_integrante = id_cargo

        integrante_motoclube = Integrantes.objects.create(nome_integrante=nome_integrante,
                                                          foto_integrante=foto_integrante,
                                                          data_entrada=data_entrada,
                                                          integrante_ativo=integrante_ativo,
                                                          cargo_integrante=cargo_integrante)
        integrante_motoclube.save()
        return redirect('integrantes')
    else:
        return render(request, 'integrantes/cria_integrante.html')


def deleta_integrante(request, id_integrante):
    """Delete um album da base de dados"""
    integrante = get_object_or_404(Integrantes, pk=id_integrante)
    integrante.delete()
    return redirect('integrantes')


def edita_integrante(request, id_integrante):
    """Edita o album selecionado"""
    integrante = get_object_or_404(Integrantes, pk=id_integrante)

    # Valida o cargo do integrante
    for id_cargo, nivel in Integrantes.NIVEL:
        if id_cargo == integrante.cargo_integrante:
            integrante.cargo_integrante = nivel

    data = integrante.data_entrada
    integrante.data_entrada = datetime.strftime(data, '%Y-%m-%d')

    dados = {
        'integrante': integrante
    }
    return render(request, 'integrantes/edita_integrante.html', dados)


def atualiza_integrante(request):
    if request.method == 'POST':
        id_integrante = request.POST['integrante.id']
        a = Integrantes.objects.get(pk=id_integrante)
        a.nome_integrante = request.POST['nome_integrante']
        a.data_entrada = request.POST['data_entrada']
        a.integrante_ativo = request.POST['integrante_ativo']
        a.cargo_integrante = request.POST['cargo_integrante']

        if 'foto_integrante' in request.FILES:
            a.foto_integrante = request.FILES['foto_integrante']

        # Valida integrante ativo
        if a.integrante_ativo == 'on':
            a.integrante_ativo = True
        else:
            a.integrante_ativo = False

        # Valida o cargo do integrante
        for id_cargo, nivel in Integrantes.NIVEL:
            if nivel == a.cargo_integrante:
                a.cargo_integrante = id_cargo

        a.save()
        return redirect('integrantes')
