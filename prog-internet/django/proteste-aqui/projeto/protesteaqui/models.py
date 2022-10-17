from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

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
    def __str__(self):
        return self.nome

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
    def __str__(self):
        # return self.professor.nome + " em " + str(self.criado_em.day) + "/" + str(self.criado_em.month) + "/" + str(self.criado_em.year) + " às " + str(self.criado_em.hour) + ":" + str(self.criado_em.minute) + ":" + str(self.criado_em.second)
        return "Avaliação a " + self.professor.nome + " em " + self.criado_em.strftime("%m/%d/%Y, %H:%M:%S")