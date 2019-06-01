from django.contrib import admin
from .models import ArtWork

class ArtWorkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'order')
    ordering =('order',)
    search_fields = ('title',)

admin.site.register(ArtWork, ArtWorkAdmin)