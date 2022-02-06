from django.shortcuts import render

def home(request):
     return render(request,'inicio.html')

def lista_cursos(request):
    cursos = ['Python','HTML','CSS','JavaScript','Java','Lógica de Programação']
    linhas = len(cursos)
    return render(request,'cursos.html',{'cursos' : cursos, 'total' : linhas})

def cadastrar_clientes(request):
     return render(request,'cadastrar-clientes.html')