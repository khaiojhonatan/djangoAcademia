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

    aluno = get_object_or_404(Alunos, cpf=cpf)
    dadosAcademia = DadosAcademia.objects.get(aluno=aluno)
    return render(request, 'template_alunos/alunos.html', {'alunos':alunos, 'dadosAcademia':dadosAcademia})
    
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

        if Alunos.objects.filter(email=email).exists():
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

        nome = request.POST.get('nome') 
        nascimento = request.POST.get('nascimento')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        rg = request.POST.get('rg')
        bairro = request.POST.get('bairro')
        rua = request.POST.get('rua')
        num_residencia = request.POST.get('num_residencia')
        
        if not nascimento or not telefone \
                or not email or not rg or not bairro \
                or not rua or not num_residencia :
            messages.error(request, "Não pode deixar campos da área de dados pessoais em branco!")
            return render(request, 'template_alunos/edit_aluno.html')
        try:
            validate_email(email)
        except:
            messages.info(request, "E-mail inválido!")
            return render(request, 'template_alunos/edit_aluno.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email já existente!")
            return render(request, 'template_alunos/edit_aluno.html')

        aluno = get_object_or_404(Alunos, cpf=cpf)
        aluno.nome = nome
        aluno.nascimento = nascimento
        aluno.telefone = telefone
        aluno.email = email
        aluno.rg = rg
        aluno.bairro = bairro
        aluno.num_residencia = num_residencia
        
        aluno.save()

        messages.success(request, "Informações do Aluno alteradas com sucesso")

        return redirect('alunos')

    aluno = get_object_or_404(Alunos, cpf=cpf)
    dadosAcademia = DadosAcademia.objects.get(aluno=aluno)
    return render(request, 'template_alunos/edit_aluno.html', {'aluno': aluno, 'dadosAcademia':dadosAcademia})

@login_required(login_url='login')
def add_medidas(request, id):
        if request.method == "POST":

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
            
            if not altura or not peso \
                    or not imc or not gordura or not liquido \
                    or not pa or not pulso or not bat_cardiaco \
                    or not quadriceps or not torax or not cintura \
                    or not culote or not biceps_D or not biceps_E \
                    or not coxa_D or not coxa_E :
                messages.error(request, "Não pode deixar campos da área de dados pessoais em branco!")
                return render(request, 'template_alunos/add_medidas.html')

            dadosAcademia = get_object_or_404(DadosAcademia, pk=id)
            dadosAcademia.dat_medidas = dat_medidas
            dadosAcademia.altura = altura
            dadosAcademia.peso = peso
            dadosAcademia.imc = imc
            dadosAcademia.gordura = gordura
            dadosAcademia.liquido = liquido
            dadosAcademia.pa = pa
            dadosAcademia.pulso = pulso
            dadosAcademia.bat_cardiaco =bat_cardiaco 
            dadosAcademia.ququadriceps =quadriceps
            dadosAcademia.torax = torax
            dadosAcademia.cintura = cintura
            dadosAcademia.culote = culote
            dadosAcademia.biceps_D = biceps_D
            dadosAcademia.biceps_E = biceps_E
            dadosAcademia.coxa_D = coxa_D
            dadosAcademia.coxa_E = coxa_E
            
            dadosAcademia.save()

            messages.success(request, "Medidas do Aluno Cadastradas com sucesso")

            return redirect('alunos')

        dadosAcademia = get_object_or_404(DadosAcademia, pk=id)
        return render(request, 'template_alunos/add_medidas.html')

@login_required(login_url='login')
def ver_medidas(request, id):
        if request.method == "POST":

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

            return redirect('alunos')

        dadosAcademia = get_object_or_404(DadosAcademia, pk=id)
        return render(request, 'template_alunos/ver_medidas.html', {'dadosAcademia':dadosAcademia})

    