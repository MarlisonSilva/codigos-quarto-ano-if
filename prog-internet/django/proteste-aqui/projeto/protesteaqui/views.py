from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

from .forms import AvaliacaoForm

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

def createAvaliacao(request):
    form = AvaliacaoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('avaliacoes')

    return render(request, 'avaliacao/form.html', {'form': form})


def updateAvaliacao(request, primakey):
    data = {}
    avaliacao = Avaliacao.objects.get(pk=primakey)
    form = AvaliacaoForm(request.POST or None, instance=avaliacao)
  
    if form.is_valid():
      form.save()
      return redirect('avaliacoes')
   
    data['form'] = form
    data['avaliacoes'] = avaliacoes
    return render(request, 'avaliacao/form.html', data)



def hora(request):
    site = "<html><body> <h1>HOME</h1> </body></html>" , datetime.now().strftime('%H:%M:%S')
    return HttpResponse(site)
    
def teste(request):
    prof = Professor.objects.get(pk=1)
    parametros = {"jogador": prof.nome, "disciplina": prof.disciplina, "idade": prof.idade}
    return render(request, 'teste.html', parametros)

def bomdia(request):
    return HttpResponse('Bom dia!')
