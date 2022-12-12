from django.shortcuts import render
from alunos.models import Alunos
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required(login_url='login')
def index(request):
    return render(request, 'templates/index.html')

@login_required(login_url='login')
def cobrancas(request):
    alunos = Alunos.objects.all()        
    return render(request,'templates/cobrancas.html', {'alunos': alunos})

@login_required(login_url='login')
def cobrancas(request, aluno_id):
    alunos = get_object_or_404(Alunos, id=aluno_id)
    if request.method == "POST":
        produto.delete()
        messages.success(
            request, f'{produto.nome.upper()} excluído(a) com sucesso!')
    return redirect('produtos')

@login_required(login_url='login')
def treinos(request):
    return render(request, 'templates/treinos.html')