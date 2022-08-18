from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Funcao)
admin.site.register(Funcionario)
admin.site.register(Horario)
admin.site.register(HorarioTrabalhoFuncionario)
admin.site.register(Diretor)
admin.site.register(Genero)
admin.site.register(Premiacao)
admin.site.register(Filme)
admin.site.register(FilmeTemPremiacao)
admin.site.register(Sala)
admin.site.register(FilmeExibidoSala)