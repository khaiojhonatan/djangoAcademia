from django import forms
from .models import Alunos

class AlunosModelForm(forms.ModelForm):
    class Meta:
        model = Alunos
        fields = ['inscricao', 'nome', 'nascimento', 'telefone', 'email', 'rg', 'cpf', 'bairro', 'rua', 'num_residencia']
