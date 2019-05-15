from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
    list_display = ('name',)
    ordering =('name',)
    search_fields = ('name',)

admin.site.register(Contact, ContactAdmin)