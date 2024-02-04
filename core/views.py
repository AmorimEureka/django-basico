from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.http import HttpResponse
from django.template import loader

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
    # prod = Produto.objects.get(id=pk)
    prod = get_object_or_404(Produto, id=pk)
    contex = {
        'produto': prod
    }
    return render(request, 'produto.html', contex)


def error404(request, ex):
    template= loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)


def error500(request):
    template= loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)