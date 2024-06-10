from django.db import models
import json

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField()
    date_of_death = models.DateField()
    birth_place = models.CharField(max_length=100)
    spouse = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    children = models.JSONField()
    
    # Substituir pelo código do pitz
    def add_children(self, children_list):
        self.children = json.dumps(children_list)
        self.save()

    def get_children(self):
        return json.loads(self.children)