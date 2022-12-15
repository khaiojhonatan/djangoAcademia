from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.validators import validate_email
from django.contrib.auth.models import  User
from django.core.paginator import Paginator
from django.contrib import messages
from alunos.models import Alunos
from django.db.models import Q



# Create your views here.
@login_required(login_url='login')
def index(request):
    return render(request, 'templates/index.html')

@login_required(login_url='login')
def cobrancas_listagem(request):
    alunos = Alunos.objects.all()        
    return render(request,'templates/cobrancas.html', {'alunos': alunos})

@login_required(login_url='login')
def cobrancas(request, aluno_id):
    if request.GET.get('termo'):
        termo = request.GET.get('termo')
        alunos = Alunos.objects.filter(Q(nome__icontains=termo)
                                          | Q(cpf__icontains=termo))
    else:
        alunos = Alunos.objects.all().order_by('-inscricao')

    paginator = Paginator(alunos, 10)
    page = request.GET.get('page')
    alunos = paginator.get_page(page)

    return render(request, 'templates/cobrancas.html', {'alunos':alunos})

@login_required(login_url='login')
def treinos(request):
    return render(request, 'templates/treinos.html')