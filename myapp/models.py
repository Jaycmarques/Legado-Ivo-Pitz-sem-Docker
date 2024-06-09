from django.db import models

# Create your models here.


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    local_nascimento = models.CharField(max_length=100)
    conjuge = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    # Se necessário, adicione outros campos como filho(s)