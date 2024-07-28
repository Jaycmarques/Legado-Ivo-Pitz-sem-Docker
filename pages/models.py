from django.db import models
from django.urls import reverse
from ordered_model.models import OrderedModel


class Page(OrderedModel):
    titulo = models.CharField(max_length=64)
    descricao = models.TextField(default='Descrição padrão')
    slug = models.SlugField(unique=True, max_length=32)
    redirect_url = models.URLField(blank=True, null=True)
    css_file = models.FileField(upload_to='page_css/', blank=True, null=True)  # Campo para CSS personalizado

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self) -> str:
        return self.titulo

    def get_absolute_url(self):
        if self.redirect_url:
            return self.redirect_url
        return reverse('pages:detalhe', kwargs={'slug': self.slug})

    def get_css_url(self):
        if self.css_file:
            return self.css_file.url
        return None
