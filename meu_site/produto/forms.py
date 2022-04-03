from django.forms import ModelForm
from .models import Categoria, Servico, Produto

class FormCategoria(ModelForm):
    class Meta:
        model = Categoria
        fields = ['id','nome']
        db_table = 'categoria'

class FormServico(ModelForm):
    class Meta:
        model = Servico
        fields = ['id','nome','valor']
        db_table = 'servico'

class FormProduto(ModelForm):
    class Meta:
        model = Produto
        fields = ['id','nome','valor','categ']
        db_table = 'produto'