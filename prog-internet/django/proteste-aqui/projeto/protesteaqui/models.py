from tabnanny import verbose
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime
# Create your models here.
class Professor(models.Model):
    class Meta:
        verbose_name_plural = "professores"
    nome = models.CharField(max_length=124, default='')
    disciplina = models.CharField(max_length=124, default='')
    cpf = models.CharField(max_length=14, default='')
    idade = models.IntegerField(
        validators=[MinValueValidator(0)]
    )
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

class Avaliacao(models.Model):
    class Meta:
        verbose_name_plural = "avaliacoes"
    descricao = models.TextField(max_length=500)        
    nota = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)