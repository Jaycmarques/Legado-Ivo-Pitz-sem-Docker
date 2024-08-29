from django.contrib import admin
from .models import Page
from ordered_model.admin import OrderedModelAdmin


@admin.register(Page)
class PageAdmin(OrderedModelAdmin):
    list_display = ('titulo', 'redirect_url', 'move_up_down_links')
    prepopulated_fields = {'slug': ('titulo',)}
