from django.shortcuts import render

from biblioteca.models import *
from django.http import Http404

# Create your views here.
def listaAutores(request):
    autores = Autor.objects.all()
    parametros = {
        'autores': autores
    }
    return render(request, 'autores/lista.html', parametros)

def detalheAutores(request, autor_id):
    try:
        autor = Autor.objects.get(pk=autor_id)
    except Autor.DoesNotExist:
        raise Http404("Autor " + str(autor_id) + " não existe")
    parametros = {
        'autor': autor
    }
    return render(request, 'autores/detalhe.html', parametros)


def listaLinguagens(request):
    linguagens = Linguagem.objects.all()
    parametros = {
        'linguagens': linguagens
    }
    return render(request, 'linguagens/lista.html', parametros)

def detalheLinguagens(request, linguagem_id):
    try:
        linguagem = Linguagem.objects.get(pk=linguagem_id)
    except Linguagem.DoesNotExist:
        raise Http404("Linguagem " + str(linguagem_id) + " não existe")
    parametros = {
        'linguagem': linguagem
    }
    return render(request, 'linguagens/detalhe.html', parametros)


def listaEdicoes(request):
    edicoes = Edicao.objects.all()
    parametros = {
        'edicoes': edicoes
    }
    return render(request, 'edicoes/lista.html', parametros)

def detalheEdicoes(request, edicao_id):
    try:
        edicao = Edicao.objects.get(pk=edicao_id)
    except Edicao.DoesNotExist:
        raise Http404("Edição " + str(edicao_id) + " não existe")
    parametros = {
        'edicao': edicao
    }
    return render(request, 'edicoes/detalhe.html', parametros)


def listaArtigos(request):
    artigos = Artigo.objects.all()
    parametros = {
        'artigos': artigos
    }
    return render(request, 'artigos/lista.html', parametros)

def detalheArtigos(request, artigo_id):
    try:
        artigo = Artigo.objects.get(pk=artigo_id)
    except Artigo.DoesNotExist:
        raise Http404("Linguagem " + str(artigo_id) + " não existe")
    parametros = {
        'artigo': artigo
    }
    return render(request, 'artigos/detalhe.html', parametros)
