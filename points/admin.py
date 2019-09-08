from django.contrib import admin
from .models import Pocitos, SanRoque, Zacateros, Oaxaca

class PocitosAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class SanRoqueAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class ZacaterosAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class OaxacaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Pocitos, PocitosAdmin)
admin.site.register(SanRoque, SanRoqueAdmin)
admin.site.register(Zacateros, ZacaterosAdmin)
admin.site.register(Oaxaca, OaxacaAdmin)