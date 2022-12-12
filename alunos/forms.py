from django import forms
from .models import Alunos

SEXO_CHOICES = (
    ('Masculino', 'Masculino'),
    ('Feminino', 'Feminino')
)

class AlunosModelForm(forms.ModelForm):
    class Meta:
        model = Alunos
        fields = ['inscricao', 'name', 'sexo', 'nascimento', 'telefone', 'email', 'rg', 'cpf', 'bairro', 'rua', 'numero']
