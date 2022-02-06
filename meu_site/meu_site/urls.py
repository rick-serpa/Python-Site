"""meu_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from re import T
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from .views import home, lista_cursos, cadastrar_clientes
from produto import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',home),
    path('lista-produto',TemplateView.as_view(template_name='lista-produtos.html')),
    path('lista-cliente',TemplateView.as_view(template_name='lista-clientes.html')),
    path('cadastro-cliente',cadastrar_clientes),
    path('lista-servico',TemplateView.as_view(template_name='lista-servicos.html')),
    path('contato',TemplateView.as_view(template_name='contato.html')),
    path('acesso',TemplateView.as_view(template_name='login.html')),
    path('cursos',lista_cursos),
    path('',home),
]
