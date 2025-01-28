import random
from django.shortcuts import render, get_object_or_404, redirect
from django.template import TemplateDoesNotExist
from django.contrib import messages  # Para exibir mensagens de sucesso
from pages.forms import DedicatoriaForm
from pages.models import Dedicatoria
from pages.models import Page
from django.core.paginator import Paginator

# View da página inicial
def home_view(request, *args, **kwargs):
    pages = Page.objects.all()
    return render(request, "pages/home.html", {'pages': pages})

# View para o formulário de criação de dedicatória
def criar_dedicatoria(request):
    if request.method == "POST":
        form = DedicatoriaForm(request.POST)
        if form.is_valid():
            form.save()
            # Exibe uma mensagem de sucesso
            messages.success(request, "Sua dedicatória foi enviada com sucesso!")
            return redirect('pages:criar-dedicatoria')  # Redireciona para a página do formulário
    else:
        form = DedicatoriaForm()

    return render(request, 'pages/criar_dedicatoria.html', {'form': form})

def get_random_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"

def dedicatorias_view(request):
    # Filtrar apenas as dedicatórias publicadas
    dedicatorias = Dedicatoria.objects.filter(is_published=True).order_by('created_at')

    # Gerar cor aleatória para cada dedicatória
    for dedicatoria in dedicatorias:
        dedicatoria.random_color = get_random_color()

    # Configuração da paginação - 12 itens por página
    paginator = Paginator(dedicatorias, 12)
    page_number = request.GET.get('page')  # Obtém o número da página da URL
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'pages/dedicatorias.html',
        {
            'page_obj': page_obj,  # Objeto da página atual para o template
        }
    )

def dedicatoria_detalhes(request, id):
    dedicatoria = get_object_or_404(Dedicatoria, id=id)
    
    # Gerar uma cor aleatória para o card de detalhes
    dedicatoria.random_color = get_random_color()
    
    # Encontrar a dedicatória anterior
    prev_dedicatoria = Dedicatoria.objects.filter(id__lt=dedicatoria.id).order_by('-id').first()
    
    # Encontrar a próxima dedicatória
    next_dedicatoria = Dedicatoria.objects.filter(id__gt=dedicatoria.id).order_by('id').first()

    return render(request, 'pages/dedicatoria_detalhes.html', {
        'dedicatoria': dedicatoria,
        'prev_dedicatoria': prev_dedicatoria,
        'next_dedicatoria': next_dedicatoria,
    })
  

# View para detalhes de uma página específica
def detalhe(request, slug):
    page = get_object_or_404(Page, slug=slug)

    # Tenta carregar o template baseado no slug
    try:
        template_name = f'pages/{slug}.html'
        # Verifica se o template existe
        return render(request, template_name, {'page': page})
    except TemplateDoesNotExist:
        # Se o template específico não existir, use um genérico
        template_name = 'pages/pages_detalhe.html'

    return render(request, template_name, {'page': page})
