from django.contrib import admin
from .models import Animal


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ['identifier', 'name', 'animal_type', 'breed', 'sex', 'status', 'entry_date', 'owner']
    list_filter = ['animal_type', 'sex', 'status', 'entry_type']
    search_fields = ['identifier', 'name', 'breed']
    ordering = ['-entry_date']
    list_per_page = 25
    readonly_fields = ['identifier', 'created_at', 'updated_at']
