from tabnanny import verbose
from django.db import models

# Create your models here.
 
class Funcao(models.Model):
    nome = models.CharField(max_length=45)
    class Meta:
        verbose_name_plural = "Funções"
    def __str__(self):
        return self.nome
 
class Funcionario(models.Model):
    nome = models.CharField(max_length=45)
    carteiraTrabalho = models.IntegerField()
    dataContratacao = models.DateField()
    salario = models.FloatField()
    class Meta:
        verbose_name_plural = "Funcionários"
    def __str__(self):
        return self.nome
 
class Horario(models.Model):
    horario = models.TimeField()
    class Meta:
        verbose_name_plural = "Horários"
    def __str__(self):
        return str(self.horario)
    
 
class HorarioTrabalhoFuncionario(models.Model):
    horario_idhorario = models.ForeignKey(Horario, on_delete=models.CASCADE)
    funcionario_idfuncionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    funcao_idfuncao = models.ForeignKey(Funcao, on_delete=models.CASCADE)
    class Meta:
        unique_together = [["horario_idhorario", "funcionario_idfuncionario"]]
        verbose_name_plural = "Horários de trabalho de funcionários"
    def __str__(self):
        return str(self.id)
 
class Diretor(models.Model):
    nome = models.CharField(max_length=45)
    class Meta:
        verbose_name_plural = "Diretores"
    def __str__(self):
        return self.nome
 
class Genero(models.Model):
    nome = models.CharField(max_length=45)
    class Meta:
        verbose_name_plural = "Gêneros"
    def __str__(self):
        return self.nome
 
class Premiacao(models.Model):
    nome = models.CharField(max_length=45)
    ano = models.IntegerField()
    class Meta:
        verbose_name_plural = "Premiações"
    def __str__(self):
        return self.nome

 
class Filme(models.Model):
    nomeBR = models.CharField(max_length=45)
    nomeEN = models.CharField(max_length=45)
    anoLancamento = models.IntegerField()
    sinopse = models.TextField()
    diretor_idDiretor = models.ForeignKey(Diretor, on_delete=models.CASCADE)
    genero_idGenero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "Filmes"
    def __str__(self):
        return self.nomeBR + "/" + self.nomeEN
     
class FilmeTemPremiacao(models.Model):    
    filme_idfilme = models.ForeignKey(Filme, on_delete=models.CASCADE)
    premiacao_idpremiacao = models.ForeignKey(Premiacao, on_delete=models.CASCADE)
    ganhou = models.BooleanField()
    class Meta:
        unique_together = [["filme_idfilme", "premiacao_idpremiacao"]]
        verbose_name_plural = "Filmes que têm premiações"
    def __str__(self):
        return self.filme_idfilme.__str__() + " - " + self.premiacao_idpremiacao.nome

class Sala(models.Model):
    nome = models.CharField(max_length=45)
    capacidade = models.IntegerField()
    class Meta:
        verbose_name_plural = "Salas"
    def __str__(self):
        return self.nome

class FilmeExibidoSala(models.Model):
    filme_idfilme = models.ForeignKey(Filme, on_delete=models.CASCADE)
    sala_idSala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    horario_idhorario = models.ForeignKey(Horario, on_delete=models.CASCADE)
    class Meta:
        unique_together = [["filme_idfilme", "horario_idhorario", "sala_idSala"]]        
        verbose_name_plural = "Filmes exibidos em sala"
    def __str__(self):
        return self.filme_idfilme.__str__() + " exibido em " + self.sala_idSala.nome
