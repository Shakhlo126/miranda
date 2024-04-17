from django.contrib import admin
from .models import (Category,
                     Politics,
                     Health,
                     Sport,
                     Design,
                     Business)
# Register your models here.
@admin.register(Category)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at')
    list_display_links = ('id', 'title')
    search_fields = ['title',]

admin.site.register(Politics)
admin.site.register(Health)
admin.site.register(Sport)
admin.site.register(Design)
admin.site.register(Business)
