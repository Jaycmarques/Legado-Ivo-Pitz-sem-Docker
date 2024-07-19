from django.contrib import admin
from pages.models import Page
from ordered_model.admin import OrderedModelAdmin


@admin.register(Page)
class ModuloAdmin(OrderedModelAdmin):
    list_display = ('titulo', 'move_up_down_links')
    prepopulated_fields = {'slug': ('titulo',)}
