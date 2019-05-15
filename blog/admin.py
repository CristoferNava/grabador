from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title',)
    ordering =('title',)
    search_fields = ('title',)

admin.site.register(Article, ArticleAdmin)
