from typing import List
from pages.models import Page


def listar_pages_ordenadas() -> List[Page]:
    '''
    Lista de páginas ordenadas por titulo
    :return:
    '''

    return list(Page.objects.order_by('titulo').all())


def encontrar_page(slug: str):
    return Page.objects.get(slug=slug)
