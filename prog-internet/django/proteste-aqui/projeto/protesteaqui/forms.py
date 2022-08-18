from dataclasses import fields
from re import M
from django import forms
from protesteaqui.models import Avaliacao

class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['professor', 'descricao', 'nota']

