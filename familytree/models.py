from django.db import models

class FamilyMember(models.Model):
    """
    - Esta classe lida com informações sobre membros da família,
      essenciais para construir as conexões na árvore genealógica.
    - O campo `id` segue o formato a.b.c.d(...)
    - O atributo `children` é uma lista de filhos.
    - O atributo `partner` corresponde ao parceiro atual do membro da família.
    - O atributo `divorced_parent` é utilizado para tratar situações em que
      um membro tem um filho de um casamento/relacionamento anterior.
    """
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255, db_index=True)
    info = models.CharField(max_length=1000, blank=True, null=True, db_index=True) 

    def __str__(self):
        return f'{self.id} -- {self.name}'

    def get_children(self):
        relationships = Relationship.objects.filter(parent=self)
        return [rel.child for rel in relationships]


class Relationship(models.Model):
    parent = models.ForeignKey(FamilyMember, related_name='children', on_delete=models.CASCADE, db_index=True)
    child = models.ForeignKey(FamilyMember, related_name='parents', on_delete=models.CASCADE, db_index=True)


    def __str__(self):
        return f'{self.parent.name} -> {self.child.name}'
