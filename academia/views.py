from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request, 'templates/index.html')

def cobrancas(request, aluno_id):
    aluno = Aluno.objects.get(id=aluno_id)
    print ("Teste")

    if request.method == "POST":
        status = 'pago'
        
    return redirect('cobrancas')


def notificacao(request):
    return render(request, 'templates/notificacao.html')

def treinos(request):
    return render(request, 'templates/treinos.html')