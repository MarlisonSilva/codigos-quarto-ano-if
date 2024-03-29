from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('professores/', views.professores, name='professores'),
    path('avaliacoes/', views.avaliacoes, name='avaliacoes'),
    path('avaliacoes/criar', views.createAvaliacao, name='createAvaliacao'), # criar avaliação   
    path('avaliacoes/editar/<int:primakey>', views.updateAvaliacao, name='updateAvaliacao'), # criar avaliação   
    path('hora/', views.hora, name='hora'),
    path('teste/', views.teste, name='teste'),
    path('bomdia/', views.bomdia, name='bomdia'),
]