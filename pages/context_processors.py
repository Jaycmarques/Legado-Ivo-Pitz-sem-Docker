from pages import facade


def listar_pages(request):
    return {'PAGES': facade.listar_pages_ordenadas()}
