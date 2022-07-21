from tabnanny import verbose
from django.db import models

# Create your models here.
class Professor(models.Model):
    class Meta:
        verbose_name_plural = "professores"
    nome = models.CharField(max_length=124, default='')
    disciplina = models.CharField(max_length=124, default='')
    cpf = models.CharField(max_length=14, default='')
    idade = models.IntegerField(default=0)