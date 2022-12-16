from django.db import models


# Create your models here.
class Alunos(models.Model):

    cpf = models.CharField(primary_key= True, max_length=13)
    inscricao = models.DateField()
    nome = models.CharField(max_length=50)
    nascimento = models.CharField(max_length=10)        
    telefone = models.CharField(max_length=25)
    email = models.CharField(max_length=80)
    rg = models.CharField(max_length=11)
    bairro = models.CharField(max_length=40)
    rua = models.CharField(max_length=80)
    num_residencia = models.CharField(max_length=10)
    divida = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nome



class DadosAcademia(models.Model):

    dat_medidas = models.CharField(blank =True, null= True, max_length=10)
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
    aluno= models.ForeignKey(Alunos,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.aluno.nome