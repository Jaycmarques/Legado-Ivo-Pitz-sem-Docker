from django.db import models
from django.urls import reverse
from ordered_model.models import OrderedModel


class Page(OrderedModel):
    titulo = models.CharField(max_length=64)
    descricao = models.TextField(default='Descrição padrão')
    slug = models.SlugField(unique=True, max_length=32)

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self) -> str:
        return self.titulo

    def get_absolute_url(self):
        return reverse('pages:detalhe', kwargs={'slug': self.slug})
