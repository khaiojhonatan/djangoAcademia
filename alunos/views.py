from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.core.paginator import Paginator
from django.core.validators import validate_email
from django.contrib.auth.models import AbstractUser, User
from django.contrib.auth.decorators import login_required
from .models import Alunos
from .forms import AlunosModelForm
# Create your views here.

# @login_required(login_url='login')  ------------------------------- DANDO ERRO AO ADICIONAR ESTÁ LINHA ----------------------------------

@login_required(login_url='login')
def alunos(request):
    if request.GET.get('termo'):
        termo = request.GET.get('termo')
        alunos = Alunos.objects.filter(Q(nome__icontains=termo)
                                          | Q(cpf__icontains=cpf))
    else:
        alunos = Alunos.objects.order_by('-id')

    paginator = Paginator(alunos, 10)
    page = request.GET.get('page')
    alunos = paginator.get_page(page)

    return render(request, 'template_alunos/alunos.html')
    
@login_required(login_url='login')
def cad_alunos(request):
    if request.method == "POST":

        if request.method == "POST":
            form = AlunosModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Cadastro salvo com sucesso!')
            return redirect('alunos')
    else:
        form = AlunosModelForm()
        return render(request, 'template_alunos/cad_alunos.html', {'form': form})


@login_required(login_url='login')
def edit_cad_aluno(request):
    if request.method == "POST":
        senha1 = request.POST.get("senha1")
        senha2 = request.POST.get("senha2")

        if not senha1 or not senha2:
            messages.error(request, "Não pode deixar as senhas em branco!")
            return render(request, 'contas/edit_cadastro.html')

        if len(senha1)<8:
            messages.error(request, "Senha muito curta!")
            return render(request, 'contas/edit_cadastro.html')

        if senha1 != senha2:
            messages.error(request, "Senhas diferentes!")
            return render(request, 'contas/edit_cadastro.html')

        user = get_object_or_404(User, username=request.user)

        user.set_password(senha1)
        user.save()

        messages.success(request, "Senha alterada com sucesso")

        return redirect('login')

    # user = get_object_or_404(User, username=request.GET.get(user.username))
    return render(request, 'contas/edit_cadastro.html')
