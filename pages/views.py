from django.shortcuts import render, get_object_or_404
from django.template import TemplateDoesNotExist
from pages.models import Page

# Create your views here.


def home_view(request, *args, **kwargs):
    pages = Page.objects.all()
    return render(request, "pages/home.html", {'pages': pages})


def detalhe(request, slug):
    page = get_object_or_404(Page, slug=slug)

    # Tenta carregar o template baseado no slug
    try:
        template_name = f'pages/{slug}.html'
        # Verifica se o template existe
        render(request, template_name, {'page': page})
    except TemplateDoesNotExist:
        # Se o template específico não existir, use um genérico
        template_name = 'pages/pages_detalhe.html'

    return render(request, template_name, {'page': page})
