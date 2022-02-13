from django.shortcuts import render

def home(request):
     return render(request,'inicio.html')

def lista_cursos(request):
    cursos = ['Python','HTML','CSS','JavaScript','Java','Lógica de Programação']
    linhas = len(cursos)
    return render(request,'cursos.html',{'cursos' : cursos, 'total' : linhas})

def cadastra_produto(request):
     return render(request,'cadastrar-produto.html')

def altera_produto(request,id):
     pass

def exclui_produto(request,id):
     pass

def lista_produtos(request):
     return render(request,'lista-produtos.html')

def lista_clientes(request):
     return render(request,'lista-clientes.html')

def cadastra_cliente(request):
     return render(request,'cadastrar-cliente.html')

def altera_cliente(request,id):
     pass

def exclui_cliente(request,id):
     pass

def lista_tipos_pessoa(request):
     return render(request,'lista-tps-pessoa.html')

def cadastra_tp_pessoa(request):
     return render(request,'cadastrar-tipos-pessoa.html')

def altera_tipos_pessoa(request,id):
     pass

def exclui_tipos_pessoa(request,id):
     pass

def lista_ufs(request):
     return render(request,'lista-uf.html')

def cadastra_uf(request):
     return render(request,'cadastrar-uf.html')

def altera_uf(request,id):
     pass

def exclui_uf(request,id):
     pass

def lista_cidades(request):
     return render(request,'lista-cidade.html')

def cadastra_cidade(request):
     return render(request,'cadastrar-cidade.html')

def altera_cidade(request,id):
     pass

def exclui_cidade(request,id):
     pass

def lista_servicos(request):
     return render(request,'lista-servicos.html')

def cadastro_servico(request):
     return render(request,'cadastrar-servico.html')

def altera_servico(request,id):
     pass

def exclui_servico(request,id):
     pass