from django import forms
from .models import Alunos, DadosAcademia

class AlunosModelForm(forms.ModelForm):
    class Meta:
        model = Alunos
        fields = ['inscricao', 'nome', 'nascimento', 'telefone', 'email', 'rg', 'cpf', 'bairro', 'rua', 'num_residencia']


class DadosAcademiaModelForm(forms.ModelForm):
    class Meta:
        model = DadosAcademia
        fields = ['dat_medidas', 'altura', 'peso', 'imc', 'gordura', 'liquido', 'pa', 'pulso', 'bat_cardiaco', 'quadriceps', 'torax',
                'cintura', 'culote', 'biceps_D', 'biceps_E', 'coxa_D', 'coxa_E', 'aluno'] 