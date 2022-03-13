from django.shortcuts import render, redirect
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
    paginator = Paginator(integrantes_motoclube, 6)
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
