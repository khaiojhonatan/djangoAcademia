from django.db import models


# Create your models here.
class DadosAcademia(models.Model):

    id_medidas = models.AutoField(db_column= 'ID', primary_key=True)
    dat_medidas = models.DateField()
    altura = models.FloatField(blank =True, null= True)
    peso = models.FloatField(blank =True, null= True)
    imc = models.FloatField(blank =True, null= True)
    gordura = models.FloatField(blank =True, null= True)
    liquido = models.FloatField(blank =True, null= True)
    pa = models.FloatField(blank =True, null= True)
    pulso = models.FloatField(blank =True, null= True)
    bat_cardiaco = models.FloatField(blank =True, null= True)
    quadriceps = models.FloatField(blank =True, null= True)
    torax = models.FloatField(blank =True, null= True)
    cintura = models.FloatField(blank =True, null= True)
    culote = models.FloatField(blank =True, null= True)
    biceps_D = models.FloatField(blank =True, null= True)
    biceps_E = models.FloatField(blank =True, null= True)
    coxa_D = models.FloatField(blank =True, null= True)
    coxa_E = models.FloatField(blank =True, null= True)

    def __str__(self):
        return self.nome

class Alunos(models.Model):

    aluno_id = models.AutoField(db_column= 'ID', primary_key=True)
    inscricao = models.DateField()
    nome = models.CharField(max_length=50)
    nascimento = models.CharField(max_length=11)        
    telefone = models.CharField(max_length=25)
    email = models.CharField(max_length=80)
    rg = models.CharField(max_length=11)
    cpf = models.CharField(max_length=16)
    bairro = models.CharField(max_length=40)
    rua = models.CharField(max_length=80)
    num_residencia = models.CharField(max_length=10)
    dadoscorporais = models.ForeignKey(DadosAcademia, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

