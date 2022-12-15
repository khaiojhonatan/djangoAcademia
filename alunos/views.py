from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.core.validators import validate_email
from django.contrib.auth.models import  User
from django.contrib.auth.decorators import login_required

from alunos.forms import AlunosModelForm
from .models import Alunos, DadosAcademia
from datetime import date
# Create your views here.

@login_required(login_url='login')
def alunos(request):
    if request.GET.get('termo'):
        termo = request.GET.get('termo')
        alunos = Alunos.objects.filter(Q(nome__icontains=termo)
                                          | Q(cpf__icontains=termo)).order_by('-nome')
    else:
        alunos = Alunos.objects.all().order_by('-nome')

    paginator = Paginator(alunos, 10)
    page = request.GET.get('page')
    alunos = paginator.get_page(page)

    return render(request, 'template_alunos/alunos.html', {'alunos':alunos})
    
@login_required(login_url='login')
def cad_alunos(request):
    if request.method == "POST":

        inscricao = date.today()
        nome = request.POST.get('nome')
        nascimento = request.POST.get('nascimento')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        rg = request.POST.get('rg')
        cpf = request.POST.get('cpf')
        bairro = request.POST.get('bairro')
        rua = request.POST.get('rua')
        num_residencia = request.POST.get('num_residencia')

        dat_medidas = request.POST.get('dat_medidas')
        altura = request.POST.get('altura')
        peso = request.POST.get('peso')
        imc = request.POST.get('imc')
        gordura = request.POST.get('gordura')
        liquido = request.POST.get('liquido')
        pa = request.POST.get('pa')
        pulso = request.POST.get('pulso')
        bat_cardiaco = request.POST.get('bat_cardiaco')
        quadriceps = request.POST.get('quadriceps')
        torax = request.POST.get('torax')
        cintura = request.POST.get('cintura')
        culote = request.POST.get('culote')
        biceps_D = request.POST.get('biceps_D')
        biceps_E = request.POST.get('biceps_E')
        coxa_D = request.POST.get('coxa_D')
        coxa_E = request.POST.get('coxa_E')

        if not nome or not nascimento or not telefone \
                or not email or not rg or not cpf or not bairro \
                or not rua or not num_residencia :
            messages.error(request, "Não pode deixar campos da área de dados pessoais em branco!")
            return render(request, 'template_alunos/cad_alunos.html')
        try:
            validate_email(email)
        except:
            messages.info(request, "E-mail inválido!")
            return render(request, 'template_alunos/cad_alunos.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email já existente!")
            return render(request, 'template_alunos/cad_alunos.html')

        

        alunos = Alunos.objects.create(inscricao = inscricao, nome=nome, nascimento=nascimento, telefone=telefone , email=email,
                                        rg=rg, cpf=cpf, bairro=bairro, rua=rua, num_residencia=num_residencia)
        alunos.save()
        dadosAcademia = DadosAcademia.objects.create(dat_medidas=dat_medidas, altura =altura, peso = peso, imc = imc, gordura = gordura,
                                    liquido = liquido, pa = pa, pulso = pulso, bat_cardiaco = bat_cardiaco, quadriceps = quadriceps,
                                    torax = torax, cintura = cintura, culote = culote, biceps_D = biceps_D, biceps_E = biceps_E,
                                    coxa_D = coxa_D, coxa_E = coxa_E,aluno=alunos)
        dadosAcademia.save()
        messages.success(request, "Registrado com sucesso!")

        return redirect('alunos')
    return render(request, 'template_alunos/cad_alunos.html')


@login_required(login_url='login')
def edit_aluno(request, cpf):
    if request.method == "POST":
        senha1 = request.POST.get("senha1")
        senha2 = request.POST.get("senha2")

        if not senha1 or not senha2:
            messages.error(request, "Não pode deixar as senhas em branco!")
            return render(request, 'template_alunos/edit_aluno.html')

        if len(senha1)<8:
            messages.error(request, "Senha muito curta!")
            return render(request, 'template_alunos/edit_aluno.html')

        if senha1 != senha2:
            messages.error(request, "Senhas diferentes!")
            return render(request, 'template_alunos/edit_aluno.html')

        user = get_object_or_404(User, username=request.user)

        user.set_password(senha1)
        user.save()

        messages.success(request, "Senha alterada com sucesso")

        return redirect('login')

    user = get_object_or_404(Alunos, pk=cpf)
    form = AlunosModelForm(request.POST or None, instance=user)
    return render(request, 'template_alunos/edit_aluno.html', {'form': form})


# def edit_aluno(request, alunos_cpf):
#     # produto = Produto.objects.get(id=produto_id)
#     alunos = get_object_or_404(Alunos, id=alunos_cpf)
#     form = AlunosModelForm(request.POST or None,
#                             request.FILES or None, instance=alunos)
#     if form.is_valid():
#         form.save()
#         messages.success(
#             request, f'{alunos.nome.upper()} editado(a) com sucesso!')
#         return redirect('alunos')
#     return render(request,
#                   'alunos/editar_alunos.html', {'alunos': alunos, 'form': form})