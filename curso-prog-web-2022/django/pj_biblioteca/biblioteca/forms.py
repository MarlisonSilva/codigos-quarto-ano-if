from dataclasses import field, fields
from pyexpat import model
from django.forms import ModelForm
from .models import *

class AutorForm(ModelForm):
    class Meta:
        model = Autor
        fields = ['nome', 'biografia', 'email']

class LinguagemForm(ModelForm):
    class Meta:
        model = Linguagem
        fields = ['nome']

class EdicaoForm(ModelForm):
    class Meta:
        model = Edicao
        fields = ['numero', 'editorial', 'data']

class ArtigoForm(ModelForm):
    class Meta:
        model = Artigo
        fields = ['titulo', 'introducao', 'autor_id', 'linguagem_id', 'edicao_id']