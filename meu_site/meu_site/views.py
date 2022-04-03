from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from numpy import ufunc
from cliente.models import Cliente, TpPessoa, UF, Cidade, EstadoCivil
from produto.models import Produto, Servico, Categoria
from cliente.forms import FormUF, FormCidade, FormTpPessoa, FormCliente, FormEstadoCivil
from produto.forms import FormCategoria, FormServico, FormProduto

def home(request):
    return render(request,'inicio.html')

@login_required
def lista_cursos(request):
    cursos = ['Python','HTML','CSS','JavaScript','Java','Lógica de Programação']
    linhas = len(cursos)
    return render(request,'cursos.html',{'cursos' : cursos, 'total' : linhas})

@login_required
def lista_categorias(request):
    pesquisa = request.GET.get('txtPesquisa')
    temPesquisa = False
    if pesquisa:
        categoria = Categoria.objects.filter(nome__icontains=pesquisa)
        temPesquisa = True
    else:
        categoria = Categoria.objects.all()
    totalCategoria = categoria.count
    return render(request,'lista-categorias.html',{'categoria' : categoria, 'total' : totalCategoria, 'pesquisa' : temPesquisa})

@login_required
def cadastra_categoria(request):
    form = FormCategoria(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(lista_categorias)
    return render(request,'cadastrar-categoria.html',{'form' : form})

@login_required
def altera_categoria(request,id):
    categoria = Categoria.objects.get(id=id)
    form = FormCategoria(request.POST,instance=categoria)

    if form.is_valid():
        form.save()
        return redirect(lista_categorias)
    
    return render(request,'alterar-categoria.html',{'form' : form,'categoria' : categoria})

@login_required
def exclui_categoria(request,id):
    categoria = Categoria.objects.get(id=id)
    if request.method == 'POST':
        categoria.delete()
        return redirect(lista_categorias)
    
    return render(request,'excluir-categoria.html',{'categoria' : categoria})

@login_required
def lista_produtos(request):
    pesquisa = request.GET.get('txtPesquisa')
    temPesquisa= False
    if pesquisa:
        produto = Produto.objects.filter(nome__icontains=pesquisa)
        temPesquisa= True
    else:
        produto = Produto.objects.all().order_by('nome')
    totalProduto = produto.count
    return render(request,'lista-produtos.html',{'produto' : produto, 'total' : totalProduto, 'pesquisa' : temPesquisa})

@login_required
def cadastra_produto(request):
    categorias = Categoria.objects.all().order_by('nome')
    form = FormProduto(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(lista_produtos)

    return render(request,'cadastrar-produto.html',{'categoria' : categorias, 'form' : form})

@login_required
def altera_produto(request,id):
    produto = Produto.objects.get(id=id)
    form = FormProduto(request.POST,instance=produto)
    categoria = Categoria.objects.get(id=produto.categ_id)
    listaCategoria = Categoria.objects.all()

    if form.is_valid():
        form.save()
        return redirect(lista_produtos)

    return render(request,'alterar-produto.html',{'produto' : produto, 'form' : form, 'categoriaProd' : categoria, 'listaCategoria' : listaCategoria})

@login_required
def exclui_produto(request,id):
    produto = Produto.objects.get(id=id)
    categoria = Categoria.objects.get(id=produto.categ_id)

    if request.method == 'POST':
        produto.delete()
        return redirect(lista_produtos)
    
    return render(request,'excluir-produto.html',{'produto' : produto, 'categoria' : categoria})

def lista_clientes(request):
    pesquisa = request.GET.get('txtPesquisa')
    temPesquisa= False
    if pesquisa:
        cliente = Cliente.objects.filter(nome__icontains=pesquisa)
        temPesquisa = True
    else:
        cliente = Cliente.objects.all()
    totalCliente = cliente.count
    return render(request,'lista-clientes.html',{'cliente' : cliente, 'total' : totalCliente,'pesquisa' : temPesquisa})

@login_required
def cadastra_cliente(request):
    cidade = Cidade.objects.all().order_by('nome')
    form = FormCliente(request.POST or None)
    estCivil = EstadoCivil.objects.all().order_by('descricao')
    estado = UF.objects.all().order_by('nome')
    if form.is_valid():
        form.save()
        return redirect(lista_clientes)

    return render(request,'cadastrar-cliente.html',{'cidade' : cidade, 'form' : form, 'estCivil' : estCivil, 'uf' : estado})

def detalha_cliente(request,id):
    cliente = Cliente.objects.get(id=id)
    cidade = Cidade.objects.all()
    cidadeCliente = Cidade.objects.get(id=cliente.cidade_id)
    return render(request,'detalhar-cliente.html',{'cliente' : cliente, 'cidade' : cidade, 'cidadeCliente' : cidadeCliente})
    
@login_required
def altera_cliente(request,id): 
    cliente = Cliente.objects.get(id=id)
    form = FormCliente(request.POST,instance=cliente)
    cidade = Cidade.objects.all()
    cidadeCliente = Cidade.objects.get(id=cliente.cidade_id)
    estCivil = EstadoCivil.objects.all()
    estCliente = cliente.EstCivil
    dtNasc = cliente.nasc.strftime('%d/%m/%Y')
    
    if form.is_valid():
        form.save()
        return redirect(lista_clientes)

    dados = {
                'form' : form, 
                'cidade' : cidade, 
                'cliente' : cliente, 
                'cidadeCliente' : cidadeCliente,
                'dtNasc' : dtNasc,
                'estCivil' : estCivil,
                'estCliente' : estCliente
            }
    return render(request,'alterar-cliente.html',dados)

@login_required
def exclui_cliente(request,id):
    cliente = Cliente.objects.get(id=id)
    cidade = Cidade.objects.get(id=cliente.cidade_id)
    estadocivil = ['Solteiro(a)','Casado(a)','Divorciado(a)','Viúvo(a)','Desquitado(a)','União Estável']
    opEstCivil = estadocivil[cliente.EstCivil-1]

    if request.method == 'POST':
        cliente.delete()
        return redirect(lista_clientes)
    
    return render(request,'excluir-cliente.html',{'cliente' : cliente, 'cidade' : cidade,'CliEstCivil' : opEstCivil})

@login_required
def lista_tipos_pessoa(request):
    pesquisa = request.GET.get('txtPesquisa')
    temPesquisa= False
    if pesquisa:
        tipo = TpPessoa.objects.filter(nome__icontains=pesquisa)
        temPesquisa= True
    else:
        tipo = TpPessoa.objects.all()
    totalTipo = tipo.count
    return render(request,'lista-tps-pessoa.html',{'tipo' : tipo, 'total' : totalTipo, 'pesquisa' : temPesquisa})

@login_required
def cadastra_tipos_pessoa(request):
    form = FormTpPessoa(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(lista_tipos_pessoa)

    return render(request,'cadastrar-tipos-pessoa.html',{'form' : form})

@login_required
def altera_tipos_pessoa(request,id):
    tipo = TpPessoa.objects.get(id=id)
    form = FormTpPessoa(request.POST,instance=tipo)

    if form.is_valid():
        form.save()
        return redirect(lista_tipos_pessoa)

    return render(request,'alterar-tipos-pessoa.html',{'form' : form, 'tipo' : tipo})

@login_required
def exclui_tipos_pessoa(request,id):
    tipo = TpPessoa.objects.get(id=id)
    if request.method == 'POST':
        tipo.delete()
        return redirect(lista_tipos_pessoa)
    return render(request,'excluir-tipos-pessoa.html',{'tipo' : tipo})

@login_required
def lista_ufs(request):
    pesquisa = request.GET.get('txtPesquisa')
    temPesquisa= False
    if pesquisa:
        uf = UF.objects.filter(nome__icontains=pesquisa)
        temPesquisa= True
    else:
        uf = UF.objects.all().order_by('nome')
    totalUF = uf.count
    return render(request,'lista-uf.html',{'uf' : uf, 'total' : totalUF,'pesquisa' : temPesquisa})

@login_required
def cadastra_uf(request):    
    form = FormUF(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(lista_ufs)
    
    return render(request,'cadastrar-uf.html',{'form' : form})

@login_required
def altera_uf(request,id):
    uf = UF.objects.get(id=id)
    form = FormUF(request.POST,instance=uf)

    if form.is_valid():
        form.save()
        return redirect(lista_ufs)
    
    return render(request,'alterar-uf.html',{'uf' : uf,'form':form})

@login_required
def exclui_uf(request,id):
    uf = UF.objects.get(id=id)
    if request.method == 'POST':
        uf.delete()
        return redirect(lista_ufs)
    return render(request,'excluir-uf.html',{'uf' : uf})

@login_required
def getCidades(request,id):
    cidades = [cidades for cidades in Cidade.objects.filter(uf_id=id)]
    return HttpResponse(str(cidades))

@login_required
def getIdCidade(request,nome):
    ids = [cidades.id for cidades in Cidade.objects.filter(nome=nome)]
    return HttpResponse(str(ids))

@login_required
def lista_cidades(request):
    pesquisa = request.GET.get('txtPesquisa')
    temPesquisa= False
    uf = UF.objects.all().order_by('nome')
    if pesquisa:
        cidade = Cidade.objects.filter(nome__icontains=pesquisa)
        temPesquisa= True
    else:
        cidade = Cidade.objects.all().order_by('nome')
    totalCidade = cidade.count
    return render(request,'lista-cidades.html',{'cidade' : cidade, 'total' : totalCidade, 'pesquisa' : temPesquisa, 'uf' : uf})

@login_required
def cadastra_cidade(request):
    uf = UF.objects.all().order_by('nome')
    form = FormCidade(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(lista_cidades)

    return render(request,'cadastrar-cidade.html',{'uf' : uf ,'form' : form})

@login_required
def altera_cidade(request,id):
    cidade = Cidade.objects.get(id=id)
    form = FormCidade(request.POST,instance=cidade)
    estado = UF.objects.all()
    uf = UF.objects.get(id=cidade.uf_id)

    if form.is_valid():
        form.save()
        return redirect(lista_cidades)
    
    return render(request,'alterar-cidade.html',{'cidade' : cidade, 'form' : form,'uf' : uf, 'estado' : estado})

@login_required
def exclui_cidade(request,id):
    cidade = Cidade.objects.get(id=id)
    estado = UF.objects.get(id=cidade.uf_id)

    if request.method == 'POST':
        cidade.delete()
        return redirect(lista_cidades)
    
    return render(request,'excluir-cidade.html',{'cidade' : cidade, 'estado' : estado})

@login_required
def lista_servicos(request):
    pesquisa = request.GET.get('txtPesquisa')
    temPesquisa= False
    if pesquisa:
        servico = Servico.objects.filter(nome__icontains=pesquisa)
        temPesquisa= True
    else:
        servico = Servico.objects.all()
    totalServicos = servico.count
    return render(request,'lista-servicos.html', {'servico' : servico, 'total' : totalServicos, 'pesquisa' : temPesquisa})

@login_required
def cadastra_servico(request):
    form = FormServico(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(lista_servicos)

    return render(request,'cadastrar-servico.html',{'form' : form})

@login_required
def altera_servico(request,id):
    servico = Servico.objects.get(id=id)
    form = FormServico(request.POST,instance=servico)

    if form.is_valid():
        form.save()
        return redirect(lista_servicos)

    return render(request,'alterar-servico.html',{'form' : form,'servico' : servico})

@login_required
def exclui_servico(request,id):
    servico = Servico.objects.get(id=id)
    if request.method == 'POST':
        servico.delete()
        return redirect(lista_servicos)
    return render(request,'excluir-servico.html',{'servico' : servico})

@login_required
def lista_EstadoCivil(request):
    pesquisa = request.GET.get('txtPesquisa')
    temPesquisa= False
    if pesquisa:
        estadoCivil = EstadoCivil.objects.filter(descricao__icontains=pesquisa)
        temPesquisa= True
    else:
        estadoCivil = EstadoCivil.objects.all().order_by('descricao')
    total = estadoCivil.count
    return render(request,'lista-EstadoCivil.html',{'estadoCivil' : estadoCivil, 'total' : total,'pesquisa' : temPesquisa})

@login_required
def cadastra_EstadoCivil(request):
    form = FormEstadoCivil(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(lista_EstadoCivil)
    
    return render(request,'cadastrar-estado-civil.html',{'form' : form})

@login_required
def altera_EstadoCivil(request,id):
    estadoCivil = EstadoCivil.objects.get(id=id)
    form = FormEstadoCivil(request.POST,instance=estadoCivil)

    if form.is_valid():
        form.save()
        return redirect(lista_EstadoCivil)
    
    return render(request,'alterar-estado-civil.html',{'estadoCivil' : estadoCivil, 'form' : form})

@login_required
def exclui_EstadoCivil(request,id):
    estadoCivil = EstadoCivil.objects.get(id=id)
    
    if request.method == 'POST':
        estadoCivil.delete()
        return redirect(lista_EstadoCivil)
    
    return render(request,'excluir-estado-civil.html',{'estadoCivil' : estadoCivil})
    
        
