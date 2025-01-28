from django.contrib import admin
from .models import Dedicatoria, Page
from ordered_model.admin import OrderedModelAdmin


@admin.register(Page)
class PageAdmin(OrderedModelAdmin):
    list_display = ('titulo', 'redirect_url', 'move_up_down_links')
    prepopulated_fields = {'slug': ('titulo',)}

@admin.register(Dedicatoria)
class DedicatoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'message', 'is_published', 'created_at')
    list_filter = ('is_published', 'created_at')
    search_fields = ('name', 'message')
    list_editable = ('is_published',)