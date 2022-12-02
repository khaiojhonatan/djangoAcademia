from django.contrib import admin
from django.urls import path
from espacofit import views

urlpatterns = [
    path('', admin.site.urls),
]