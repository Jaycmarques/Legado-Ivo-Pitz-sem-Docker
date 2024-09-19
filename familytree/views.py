from django.shortcuts import render
from .models import FamilyMember


def familytree(request):
    family_members = FamilyMember.objects.all()  # Recupera todos os membros da família
    return render(request, 'familytree/index.html', {'family_members': family_members})


def detail(request):
    member_id = request.GET.get('id')
    try:
        member = FamilyMember.objects.get(id=member_id)
        children = member.children()  # Chama o método que retorna os filhos
        return render(request, 'familytree/familymember.html', {'member': member, 'children': children})
    except FamilyMember.DoesNotExist:
        return render(request, 'familytree/familymember.html', {'error': 'Membro não encontrado.'})
