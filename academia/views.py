from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def index(request):
    return render(request, 'templates/index.html')

@login_required(login_url='login')
def cobrancas(request, Alunos_id, Alunos_divida):
    Alunos = Alunos.objects.get(id=Alunos_id, divida=Alunos_divida)

    if request.method == "POST" and Alunos_divida == True:
        Alunos_divida = False
        

    return render(request,'templates/cobrancas.html', {Alunos_id: Alunos_id, Alunos_divida: Alunos_divida})

@login_required(login_url='login')
def treinos(request):
    return render(request, 'templates/treinos.html')