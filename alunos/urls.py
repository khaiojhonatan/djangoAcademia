from django.urls import path
from . import views

urlpatterns = [
    path('alunos/', views.alunos, name='alunos'),
    path('cad_alunos/', views.cad_alunos, name='cad_alunos'),
    path('edit_aluno/<str:cpf>', views.edit_aluno, name='editar_aluno'),
    path('add_medidas/<int:id>', views.add_medidas, name='add_medidas'),
    path('ver_medidas/<int:id>', views.ver_medidas, name='ver_medidas'),
]
