from django.db import models


class FamilyMember(models.Model):
    """
    - This class handles information about family members
     which are essential to build the tree connections.
    - The id field follows the format a.b.c.d(...)
    - The children attribute consists of a list of children
    - Partner corresponds to the current partner of the
    family member in the blood line.
    - The divorcedParent attribute is used to handle situations
    where a member has a child from a previous marriage/relationship,
    so it is associated with the child's name (i.e: John had a son with
    Jessica called Steve, but now John is married to Katherin. So when
    displaying Steve on the tree under John's name we want to display
    "Steve (son of Jessica) rather than simply Steve."
    """
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    partner = models.CharField(max_length=255, blank=True, null=True)
    divorced_parent = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.id} -- {self.name}'

    def get_children(self):
        # Filtra as relações e retorna apenas os filhos
        relationships = Relationship.objects.filter(parent=self)
        return [rel.child for rel in relationships]


class Relationship(models.Model):
    parent = models.ForeignKey(FamilyMember, related_name='children', on_delete=models.PROTECT)
    child = models.ForeignKey(FamilyMember, related_name='parents', on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.parent.name} -> {self.child.name}'
