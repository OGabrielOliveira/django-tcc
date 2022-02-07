from django.urls import path

from .view import site
from .view import login

app_name = 'moodle'
urlpatterns = [
    path('',site.index, name='index'),
    path('sobre', site.sobre, name='sobre'),
    path('termos', site.termos, name='termos'),
    path('privacidade', site.privacidade, name='privacidade'),

    path('login', login.login, name='login'),
    path('cadastro', login.cadastro, name='cadastro'),
]
