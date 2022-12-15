from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.index, name='index'),
    path('cobrancas_listagem/', views.cobrancas_listagem, name='cobrancas_listagem'),
    path('cobrancas/<str:cpf>', views.cobrancas, name='cobrancas'),
    path('treinos/', views.treinos, name='treinos'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)