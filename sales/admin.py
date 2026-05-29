from django.contrib import admin
from .models import Sale


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ['id', 'client_name', 'description', 'quantity', 'unit_price', 'total_price_display', 'date', 'owner']
    list_filter = ['date']
    search_fields = ['client_name', 'description']
    ordering = ['-date']

    def total_price_display(self, obj):
        return f"{obj.total_price:,.0f} FCFA"
    total_price_display.short_description = "Total"
