from django.contrib import admin

from .models import Structure, Region


class StructureAdmin(admin.ModelAdmin):
    list_display = ('region', 'country', 'value')
    search_fields = ['country']


class RegionAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Structure, StructureAdmin)
admin.site.register(Region, RegionAdmin)
