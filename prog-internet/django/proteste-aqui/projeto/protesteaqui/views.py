import site
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

from .models import Professor, Avaliacao

# Create your views here.

def index(request):
    return HttpResponse('Olá!')

def professores(request):
    professores = Professor.objects.all()
    parametros = { "professores": professores }
    return render(request, 'professor/index.html', parametros)

def avaliacoes(request):
    avaliacoes = Avaliacao.objects.all()
    parametros = { "avaliacoes": avaliacoes }
    return render(request, 'avaliacao/index.html', parametros)

def hora(request):
    site = "<html><body> <h1>HOME</h1> </body></html>" , datetime.now().strftime('%H:%M:%S')
    return HttpResponse(site)
    
def teste(request):
    prof = Professor.objects.get(pk=1)
    parametros = {"jogador": prof.nome, "disciplina": prof.disciplina, "idade": prof.idade}
    return render(request, 'teste.html', parametros)

def bomdia(request):
    return HttpResponse('Bom dia!')
