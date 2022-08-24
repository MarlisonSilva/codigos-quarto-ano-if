from django.shortcuts import render, redirect

from biblioteca.models import *
from .forms import *

# Create your views here.
# ---------- AUTORES ----------
def listarAutores(request):
    autores = Autor.objects.all()
    parametros = {
        'autores': autores        
    }
    return render(request, 'autores/listar.html', parametros)

def criarAutores(request):
    form = AutorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listarAutores')
    parametros = {
        'form': form        
    }
    return render(request, 'autores/form.html', parametros)

def editarAutores(request, pk):
    autor = Autor.objects.get(pk=pk)
    form = AutorForm(request.POST or None, instance=autor)
    if form.is_valid():
        form.save()
        return redirect('listarAutores')
    parametros = {
        'form': form,
        'autor': autor
    }
    return render(request, 'autores/form.html', parametros)

def deletarAutores(request, pk):
    autor = Autor.objects.get(pk=pk)
    autor.delete()
    return redirect('listarAutores')

# ---------- LINGUAGENS ----------
def listarLinguagens(request):
    linguagens = Linguagem.objects.all()
    parametros = {
        'linguagens': linguagens
    }
    return render(request, 'linguagens/listar.html', parametros)

def criarLinguagens(request):
    form = LinguagemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listarLinguagens')
    parametros = {
        'form': form        
    }
    return render(request, 'linguagens/form.html', parametros)

def editarLinguagens(request, pk):
    linguagem = Linguagem.objects.get(pk=pk)
    form = LinguagemForm(request.POST or None, instance=linguagem)
    if form.is_valid():
        form.save()
        return redirect('listarLinguagens')
    parametros = {
        'form': form,
        'linguagem': linguagem   
    }
    return render(request, 'linguagens/form.html', parametros)

def deletarLinguagens(request, pk):
    linguagem = Linguagem.objects.get(pk=pk)
    linguagem.delete()
    return redirect('listarLinguagens')

# ---------- EDIÇÕES ----------
def listarEdicoes(request):
    edicoes = Edicao.objects.all()
    parametros = {
        'edicoes': edicoes
    }
    return render(request, 'edicoes/listar.html', parametros)

def criarEdicoes(request):
    form = EdicaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listarEdicoes')
    parametros = {
        'form': form        
    }
    return render(request, 'edicoes/form.html', parametros)

def editarEdicoes(request, pk):
    edicao = Edicao.objects.get(pk=pk)
    form = EdicaoForm(request.POST or None, instance=edicao)
    if form.is_valid():
        form.save()
        return redirect('listarEdicoes')
    parametros = {
        'form': form,
        'edicao': edicao   
    }
    return render(request, 'edicoes/form.html', parametros)

def deletarEdicoes(request, pk):
    edicao = Edicao.objects.get(pk=pk)
    edicao.delete()
    return redirect('listarEdicoes')

# ---------- ARTIGOS ----------
def listarArtigos(request):
    artigos = Artigo.objects.all()
    parametros = {
        'artigos': artigos
    }
    return render(request, 'artigos/listar.html', parametros)

def criarArtigos(request):
    form = ArtigoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listarArtigos')
    parametros = {
        'form': form        
    }
    return render(request, 'artigos/form.html', parametros)

def editarArtigos(request, pk):
    artigo = Artigo.objects.get(pk=pk)
    form = ArtigoForm(request.POST or None, instance=artigo)
    if form.is_valid():
        form.save()
        return redirect('listarArtigos')
    parametros = {
        'form': form,
        'artigo': artigo   
    }
    return render(request, 'artigos/form.html', parametros)

def deletarArtigos(request, pk):
    artigo = Autor.objects.get(pk=pk)
    artigo.delete()
    return redirect('listarArtigos')