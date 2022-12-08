from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request, 'templates/index.html')

def alunos(request):
    return render(request, 'templates/alunos.html')

def perfil(request):
    return render(request, 'templates/perfil.html')