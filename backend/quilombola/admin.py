from django.contrib import admin
from quilombola.models import Community


@admin.register(Community)
class QuilombolaAdmin(admin.ModelAdmin):
    list_display = ('name', 'area', 'family_no', 'city')
