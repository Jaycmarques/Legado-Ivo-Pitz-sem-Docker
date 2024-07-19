from django.shortcuts import render
from pages import facade

# Create your views here.


def home_view(request, *args, **kwargs):
    return render(request, "pages/home.html")


def detalhe(request, slug):
    page = facade.encontrar_page(slug)
    return render(request, 'pages/pages_detalhe.html', {'page': page})
