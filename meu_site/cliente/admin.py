from csv import list_dialects
from django.contrib import admin
from .models import TpPessoa, CPFCNPJ, UF, Cidade, Cliente
# Register your models here.

class VisualizaCliente(admin.ModelAdmin):
    list_display = ['id','nome','cpfcnpj','EstCivil']
    list_display_links = ['id','nome']
    list_per_page = 5
    search_fields = ['nome']
    # fields = ['nome','email']
    # list_filter = ['nome','cpfcnpj']
    fieldsets = [
        ('Básico',{'fields':('nome','cpfcnpj','sexo','nasc','EstCivil')}),
        ('Opcional',{'fields':('filhos','cidade','carro',)}),
        ('Financeiro',{'fields':('profissao','renda',)}),
    ]


admin.site.register(TpPessoa)
admin.site.register(CPFCNPJ)
admin.site.register(UF)
admin.site.register(Cidade)
admin.site.register(Cliente,VisualizaCliente)
