from django.contrib import admin
from django.db.models import Q, Func, Value
from django.shortcuts import render

from .models import FamilyMember, Relationship


class RelationshipInline(admin.TabularInline):
    model = Relationship
    fk_name = 'parent'


class FamilyMemberAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]
    search_fields = ('id', 'name')


admin.site.register(FamilyMember, FamilyMemberAdmin)


