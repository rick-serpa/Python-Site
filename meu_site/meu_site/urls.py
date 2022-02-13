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
from .views import home, lista_cursos, cadastra_cliente, lista_tipos_pessoa, lista_ufs, lista_cidades, lista_clientes, lista_produtos, cadastra_produto, lista_servicos
from .views import cadastro_servico, cadastra_tp_pessoa, cadastra_uf, cadastra_cidade
from produto import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',home),
    path('lista-produto',lista_produtos),
    path('lista-cliente',TemplateView.as_view(template_name='lista-clientes.html')),
    path('cadastro-cliente',cadastra_cliente),
    path('cadastro-produto',cadastra_produto),
    path('lista-servico',lista_servicos),
    path('lista-tp-pessoa',lista_tipos_pessoa),
    path('lista-uf',lista_ufs),
    path('cadastro-cidade',cadastra_cidade),
    path('cadastro-tp-pessoa',cadastra_tp_pessoa),
    path('cadastro-uf',cadastra_uf),
    path('cadastro-servico', cadastro_servico),
    path('lista-clientes',lista_clientes),
    path('lista-cidade',lista_cidades),
    path('contato',TemplateView.as_view(template_name='contato.html')),
    path('acesso',TemplateView.as_view(template_name='login.html')),
    path('cursos',lista_cursos),
    path('',home),
]
