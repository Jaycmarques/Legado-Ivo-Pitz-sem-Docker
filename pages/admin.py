from django.contrib import admin
from .models import Dedicatoria, Page
from django_summernote.admin import SummernoteModelAdmin
from ordered_model.admin import OrderedModelAdmin


@admin.register(Page)
class PageAdmin(OrderedModelAdmin):
    list_display = ('titulo', 'redirect_url', 'move_up_down_links')
    prepopulated_fields = {'slug': ('titulo',)}

@admin.register(Dedicatoria)
class DedicatoriaAdmin(SummernoteModelAdmin):
    list_display = ('id', 'name', 'short_message', 'is_published', 'created_at')
    list_filter = ('is_published', 'created_at')
    search_fields = ('name', 'message')
    list_editable = ('is_published',)
    summernote_fields = ('message',)

    # Adicionando uma função para truncar a mensagem
    def short_message(self, obj):
        return obj.message[:50]  # Mostra apenas os primeiros 100 caracteres
    short_message.short_description = 'Mensagem'  # Título da coluna