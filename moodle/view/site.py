from django.shortcuts import render


def index(request):
    return render(request, 'site/index.html')

def sobre(request):
    return render(request, 'site/sobre.html', {'title': 'Sobre', 'sobre':True})

def termos(request):
    return render(request, 'site/termos.html', {'title': 'Termos', 'termos':True})

def privacidade(request):
    return render(request, 'site/privacidade.html', {'title': 'Privacidade', 'privacidade':True})
