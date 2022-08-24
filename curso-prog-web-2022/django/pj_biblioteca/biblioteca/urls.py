from django.urls import path
from . import views
urlpatterns = [
    path('autores/', views.listarAutores, name='listarAutores'),
    path('autores/criar', views.criarAutores, name='criarAutores'),
    path('autores/editar/<int:pk>', views.editarAutores, name='editarAutores'),
    path('autores/del/<int:pk>', views.deletarAutores, name='deletarAutores'),

    path('linguagens/', views.listarLinguagens, name='listarLinguagens'),
    path('linguagens/criar', views.criarLinguagens, name='criarLinguagens'),
    path('linguagens/editar/<int:pk>', views.editarLinguagens, name='editarLinguagens'),
    path('linguagens/del/<int:pk>', views.deletarLinguagens, name='deletarLinguagens'),

    path('edicoes/', views.listarEdicoes, name='listarEdicoes'),    
    path('edicoes/criar', views.criarEdicoes, name='criarEdicoes'),
    path('edicoes/editar/<int:pk>', views.editarEdicoes, name='editarEdicoes'),
    path('edicoes/del/<int:pk>', views.deletarEdicoes, name='deletarEdicoes'),

    path('artigos/', views.listarArtigos, name='listarArtigos'),
    path('artigos/criar', views.criarArtigos, name='criarArtigos'),
    path('artigos/editar/<int:pk>', views.editarArtigos, name='editarArtigos'),
    path('artigos/del/<int:pk>', views.deletarArtigos, name='deletarArtigos'),
]