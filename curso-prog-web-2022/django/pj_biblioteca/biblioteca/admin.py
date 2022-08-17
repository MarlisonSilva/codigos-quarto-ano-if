from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Autor)
admin.site.register(Linguagem)
admin.site.register(Edicao)
admin.site.register(Artigo)
