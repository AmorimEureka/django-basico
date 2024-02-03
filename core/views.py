from django.shortcuts import render

def index(request):
    if str(request.user) == 'rafaelamorim':
        var = f'Seja Bem-Vindo {request.user}'
    else:
        var = 'Usuário não está logado'
    
    context={'logado':var}

    return render(request, 'index.html', context)


def contato(request):
    return render(request,'contato.html')
