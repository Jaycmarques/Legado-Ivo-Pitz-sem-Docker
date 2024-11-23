from django.shortcuts import render
from .models import FamilyMember, Relationship
from django.db.models import Q


def familytree(request):
    # Recupera todos os membros da família, ordenados pelo ID
    family_members = FamilyMember.objects.all().order_by('id')  # Order by 'id' to display in hierarchy
    return render(request, 'familytree/index.html', {'family_members': family_members})

def detail(request):
    member_id = request.GET.get('id')
    try:
        member = FamilyMember.objects.get(id=member_id)
        children = member.children.all()  # Chama o método que retorna os filhos
        return render(request, 'familytree/familymember.html', {'member': member, 'children': children})
    except FamilyMember.DoesNotExist:
        return render(request, 'familytree/familymember.html', {'error': 'Membro não encontrado.'})


def search_family_member(request):
    search_value = request.GET.get('search', '').strip()
    
    # Busca nos campos relevantes
    family_members = (
        FamilyMember.objects.filter(
            Q(id__icontains=search_value) |
            Q(name__icontains=search_value) |
            Q(partner__icontains=search_value) |
            Q(divorced_parent__icontains=search_value)
        )
    )

    return render(
        request,
        'familytree/index.html',  
        {
            'family_members': family_members,
            'search_value': search_value,
        }
    )
