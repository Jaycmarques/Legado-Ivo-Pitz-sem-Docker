from django.shortcuts import render
from pages import facade
from pages.models import Page

# Create your views here.


def home_view(request, *args, **kwargs):
    pages = Page.objects.all()
    return render(request, "pages/home.html", {'pages': pages})


def detalhe(request, slug):
    page = facade.encontrar_page(slug)
    return render(request, 'pages/pages_detalhe.html', {'page': page})
