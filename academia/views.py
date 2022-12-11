from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request, 'templates/index.html')

def cobrancas(request):
    return render(request, 'templates/cobrancas.html')

def treinos(request):
    return render(request, 'templates/treinos.html')