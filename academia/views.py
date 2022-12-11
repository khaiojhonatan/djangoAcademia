from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request, 'templates/index.html')

def cobrancas(request, Alunos_id, Alunos_divida):
    Alunos =Alunos.objects.get(id=Alunos_id)

    if request.method == "POST" and Alunos_divida == True:
        Alunos_divida = False
        
    return render(request,'templates/cobrancas.html', {Alunos_id: Alunos_id, Alunos_divida: Alunos_divida})


def notificacao(request):
    return render(request, 'templates/notificacao.html')

def treinos(request):
    return render(request, 'templates/treinos.html')