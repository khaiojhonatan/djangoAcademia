from django.urls import path
from . import views

urlpatterns = [
    path('alunos/', views.alunos, name='alunos'),
    path('cad_alunos/', views.cad_alunos, name='cad_alunos'),
    path('edit_aluno/<str:cpf>', views.edit_aluno, name='editar_aluno'),
]
