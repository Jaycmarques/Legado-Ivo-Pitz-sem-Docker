from django.db import models
from django.urls import reverse
from ordered_model.models import OrderedModel


class Page(OrderedModel):
    titulo = models.CharField(max_length=64)
    descricao = models.TextField(default='Descrição padrão')
    slug = models.SlugField(unique=True, max_length=32)
    redirect_url = models.URLField(blank=True, null=True)
    imagem = models.ImageField(upload_to='page_images/', blank=True, null=True)  # Campo para imagem

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self) -> str:
        return self.titulo

    def get_absolute_url(self):
        if self.redirect_url:
            return self.redirect_url
        return reverse('pages:detalhe', kwargs={'slug': self.slug})

    
class Dedicatoria(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome")
    message = models.TextField(verbose_name="Mensagem")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Envio")
    is_published = models.BooleanField(default=False, verbose_name="Publicado?")

    def __str__(self):
        return f"Dedicatória de {self.name}"
