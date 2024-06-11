from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField()
    date_of_death = models.DateField(null=True, blank=True)
    birth_place = models.CharField(max_length=100)
    spouse = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True, related_name='spouses'
    )
    parent = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children'
    )

    def __str__(self):
        return self.name

    # Substituir pelo código do pitz
    def add_child(self, child):
        child.parent = self
        child.save()
