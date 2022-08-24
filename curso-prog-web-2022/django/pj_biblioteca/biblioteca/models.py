from django.db import models
from django.core.validators import MaxValueValidator
# Create your models here.
class Autor(models.Model):
    nome = models.CharField(max_length=200)
    biografia = models.TextField()
    email = models.EmailField(max_length=200)
    
    class Meta():
        verbose_name_plural = 'autores'
    def __str__(self):
        return self.nome

class Linguagem(models.Model):
    nome = models.CharField(max_length=200)
    
    class Meta():        
        verbose_name_plural = 'linguagens'
    def __str__(self):
        return self.nome

class Edicao(models.Model):
    numero = models.IntegerField(primary_key=True,
        validators=[MaxValueValidator(11)]
    )
    editorial = models.TextField()
    data = models.DateField()
    
    class Meta():        
        verbose_name_plural = 'edições'
    def __str__(self):
        return 'Edição ' + str(self.numero) + ' do editorial ' + self.editorial

class Artigo(models.Model):
    autor_id = models.ForeignKey(Autor, on_delete=models.CASCADE)
    linguagem_id = models.ForeignKey(Linguagem, on_delete=models.CASCADE)
    edicao_id = models.ForeignKey(Edicao, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    introducao = models.TextField()

    class Meta():        
        verbose_name_plural = 'artigos'
    def __str__(self):
        return self.titulo + ' de ' + self.autor_id.nome
