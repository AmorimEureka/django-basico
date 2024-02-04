from django.shortcuts import render

from .models import Produto

def index(request):
    produtos = Produto.objects.all()

    if str(request.user) == 'rafaelamorim':
        var = f'Seja Bem-Vindo {request.user}'
    else:
        var = 'Usuário não está logado'
    
    context={
        'logado':var,
        'produtos': produtos}

    return render(request, 'index.html', context)


def contato(request):
    return render(request,'contato.html')

def produto(request, pk):
    prod = Produto.objects.get(id=pk)
    contex = {
        'produto': prod
    }
    return render(request, 'produto.html', contex)