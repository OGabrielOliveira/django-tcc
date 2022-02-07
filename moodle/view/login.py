from django.shortcuts import render


def login(request):
    return render(request, 'login/login.html')

def cadastro(request):
    return render(request, 'login/cadastro.html')
