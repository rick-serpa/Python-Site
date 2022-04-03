from django.contrib import admin
from .models import TpPessoa, CPFCNPJ, UF, Cidade, Cliente

# Register your models here.
class VisualizaCliente(admin.ModelAdmin):
    list_display = ['id','nome','cpfcnpj','EstCivil',]  
    list_display_links = ['id','nome']  
    list_per_page = 4
    search_fields = ['nome','email']
    # fields = ['nome','email','EstCivil']
    fieldsets = (
        ('Básico',{'fields':('nome','cpfcnpj','sexo','nasc','EstCivil')}),
        ('Opcional',{'fields':('filhos','cidade','carro')}),
        ('Financeiro',{'fields':('profissao','renda')}),
    )
    # list_filter = ['nome',  'email','cpfcnpj']
    

admin.site.register(TpPessoa)
admin.site.register(CPFCNPJ)
admin.site.register(UF)
admin.site.register(Cidade)
admin.site.register(Cliente,VisualizaCliente)