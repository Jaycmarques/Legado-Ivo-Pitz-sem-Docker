from django.core.management.base import BaseCommand
from familytree.models import FamilyMember, Relationship


class Command(BaseCommand):
    help = 'Populate family tree from familyData.txt'

    def handle(self, *args, **kwargs):
        family = []
        with open('/home/jcmarques/.ssh/Legado-Ivo-Pitz/familytree/familyData.txt') as file:
            lines = file.readlines()
            for line in lines:
                parts = line.strip().split(" - ")
                id = parts[0]
                name = parts[1].split(",")[0].strip()
                partner_name = parts[1].split(",")[1].strip() if len(parts[1].split(",")) > 1 else None
                married = line.lower().replace("casada", "casado")
                married = married.replace("-", ",")
                married = married.lower().split("casado com")

                if len(married) > 1:
                    married = married[1].split(",")[0]
                    partner_name = married.title().strip()
                try:
                    # Tenta buscar o FamilyMember pelo id
                    member = FamilyMember.objects.get(id=id)
                    # Se encontrado, atualiza os campos relevantes
                    member.name = name
                    member.partner = partner_name
                    member.save()
                except FamilyMember.DoesNotExist:
                    # Se não existir, cria um novo FamilyMember
                    member = FamilyMember.objects.create(id=id, name=name, partner=partner_name)

                family.append(member)

        for parent in family:
            parent_id = parent.id
            for child in family:
                child_id = child.id
                # Verifica se o ID do filho segue o formato do pai
                if child_id.startswith(f"{parent_id}."):
                    try:
                        # Extrai o número do filho do ID
                        child_number = int(child_id[len(parent_id) + 1:])
                        if child_number >= 1:
                            Relationship.objects.create(parent=parent, child=child)
                    except ValueError:
                        # Se não for um número válido, ignora o ID
                        continue

        self.stdout.write(self.style.SUCCESS('Successfully populated family tree'))
