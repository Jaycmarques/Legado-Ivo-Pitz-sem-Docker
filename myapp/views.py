from django.shortcuts import render
from .models import Pessoa
# Create your views here.


def home(request):
    return render(request, 'home.html')


def arvore_genealogica(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'arvore_genealogica.html', {'pessoas': pessoas})