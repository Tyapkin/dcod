from django.contrib import admin

from .models import Structure


class StructureAdmin(admin.ModelAdmin):
    list_display = ('region', 'country', 'value')

admin.site.register(Structure, StructureAdmin)
