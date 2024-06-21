from django.contrib import admin
from .models import FamilyMember, Relationship


class RelationshipInline(admin.TabularInline):
    model = Relationship
    fk_name = 'parent'


class FamilyMemberAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]


admin.site.register(FamilyMember, FamilyMemberAdmin)
