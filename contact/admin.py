from django.contrib import admin
from .models import Contact

# Register your models here.


@admin.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'email', 'created_at')
    list_display_links = ('id', 'first_name', 'email', 'created_at')
    search_fields = ['first_name', 'email']



