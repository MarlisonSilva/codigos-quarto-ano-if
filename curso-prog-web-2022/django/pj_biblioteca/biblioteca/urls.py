from django.urls import path
from . import views
urlpatterns = [
    path('autores/', views.listaAutores, name='listaAutores'),
    path('autor/<int:autor_id>/', views.detalheAutores, name='detalheAutores'),

    path('linguagens/', views.listaLinguagens, name='listaLinguagens'),
    path('linguagem/<int:linguagem_id>/', views.detalheLinguagens, name='detalheLinguagens'),

    path('edicoes/', views.listaEdicoes, name='listaEdicoes'),
    path('edicao/<int:edicao_id>/', views.detalheEdicoes, name='detalheEdicoes'),

    path('artigos/', views.listaArtigos, name='listaArtigos'),
    path('artigo/<int:artigo_id>/', views.detalheArtigos, name='detalheArtigos'),

]