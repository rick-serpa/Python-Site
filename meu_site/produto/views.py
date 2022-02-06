from django.shortcuts import render

# Create your views here.
def lista_produtos(request):
    return render(request,'lista-produtos.html')