from django.urls import path
from . import views

urlpatterns = [
    path('', views.sign_in, name='login'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('logout/', views.logout, name='logout'),
    path('edit_cadastro/', views.edit_cadastro, name='edit_cadastro'),
]
