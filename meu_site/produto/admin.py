from django.contrib import admin
from .models import Produto, Categoria, Servico

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Produto)
admin.site.register(Servico)