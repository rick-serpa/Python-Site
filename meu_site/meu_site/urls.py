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
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from .views import cadastra_cidade, cadastra_servico, home, lista_cursos, cadastra_cliente, lista_tipos_pessoa, lista_ufs, lista_cidades
from .views import lista_clientes, lista_produtos, cadastra_produto, lista_servicos, cadastra_tipos_pessoa, detalha_cliente
from .views import cadastra_uf, altera_cidade, altera_produto, altera_cliente, altera_servico, altera_tipos_pessoa, altera_uf
from .views import exclui_cidade, exclui_cliente, exclui_produto, exclui_servico, exclui_tipos_pessoa, exclui_uf
from .views import lista_categorias, altera_categoria, exclui_categoria, cadastra_categoria, lista_EstadoCivil, altera_EstadoCivil
from .views import exclui_EstadoCivil, cadastra_EstadoCivil, getCidades, getIdCidade
from produto import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',home,name='home'),
    path('lista-categoria',lista_categorias,name='lista-categoria'),
    path('cadastro-categoria',cadastra_categoria,name='cadastro-categoria'),
    path('altera-categoria/<int:id>',altera_categoria),
    path('exclui-categoria/<int:id>',exclui_categoria),
    path('lista-produto',lista_produtos,name='lista-produto'),
    path('cadastro-produto',cadastra_produto,name='cadastro-produto'),
    path('altera-produto/<int:id>',altera_produto),
    path('exclui-produto/<int:id>',exclui_produto),
    path('lista-cliente',lista_clientes,name='lista-cliente'),
    path('cadastro-cliente',cadastra_cliente,name='cadastro-cliente'),
    path('detalha-cliente/<int:id>',detalha_cliente),
    path('altera-cliente/<int:id>',altera_cliente),
    path('exclui-cliente/<int:id>',exclui_cliente),
    path('lista-servico',lista_servicos,name='lista-servico'),
    path('cadastro-servico',cadastra_servico,name='cadastro-servico'),
    path('altera-servico/<int:id>',altera_servico),
    path('exclui-servico/<int:id>',exclui_servico),
    path('lista-tp-pessoa',lista_tipos_pessoa,name='lista-tp-pessoa'),
    path('cadastro-tp-pessoa',cadastra_tipos_pessoa,name='cadastro-tp-pessoa'),
    path('altera-tp-pessoa/<int:id>',altera_tipos_pessoa),
    path('exclui-tp-pessoa/<int:id>',exclui_tipos_pessoa),
    path('lista-uf',lista_ufs,name='lista-uf'),
    path('cadastro-uf',cadastra_uf,name='cadastro-uf'),
    path('altera-uf/<int:id>',altera_uf),
    path('exclui-uf/<int:id>',exclui_uf),
    path('getCidades/<int:id>',getCidades),
    path('getIds/<str:nome>',getIdCidade),
    path('lista-cidade',lista_cidades,name='lista-cidade'),
    path('cadastro-cidade',cadastra_cidade,name='cadastro-cidade'),
    path('altera-cidade/<int:id>',altera_cidade),
    path('exclui-cidade/<int:id>',exclui_cidade),
    path('lista-estado-civil',lista_EstadoCivil,name='lista-estado-civil'),
    path('cadastro-estado-civil',cadastra_EstadoCivil,name='cadastro-estado-civil'),
    path('altera-estado-civil/<int:id>',altera_EstadoCivil),
    path('exclui-estado-civil/<int:id>',exclui_EstadoCivil),
    path('contato',TemplateView.as_view(template_name='contato.html'),name='contato'),
    path('login',TemplateView.as_view(template_name='registration/login.html'),name='login'),
    path('logout',TemplateView.as_view(template_name='registration/logged_out.html'),name='logout'),
    path('cursos',lista_cursos,name='cursos'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('',home),
]
