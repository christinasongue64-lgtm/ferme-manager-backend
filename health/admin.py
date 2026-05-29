from django.contrib import admin
from .models import HealthRecord


@admin.register(HealthRecord)
class HealthRecordAdmin(admin.ModelAdmin):
    list_display = ['animal', 'record_type', 'date', 'description', 'medication', 'cost', 'next_date', 'owner']
    list_filter = ['record_type', 'date']
    search_fields = ['description', 'medication', 'animal__identifier']
    ordering = ['-date']
    list_per_page = 25
