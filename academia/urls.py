from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.index, name='index'),
    path('alunos/', views.alunos, name='alunos'),
    path('perfil/', views.perfil, name='perfil'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)