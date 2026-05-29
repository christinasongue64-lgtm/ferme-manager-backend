from django.contrib import admin
from .models import StockItem, StockMovement


@admin.register(StockItem)
class StockItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'quantity', 'unit', 'min_quantity', 'unit_price', 'supplier', 'is_low', 'owner']
    list_filter = ['category']
    search_fields = ['name', 'supplier']
    ordering = ['category', 'name']

    def is_low(self, obj):
        return obj.is_low
    is_low.boolean = True
    is_low.short_description = 'Stock bas ?'


@admin.register(StockMovement)
class StockMovementAdmin(admin.ModelAdmin):
    list_display = ['item', 'movement_type', 'quantity', 'date', 'reason', 'owner']
    list_filter = ['movement_type', 'date']
    search_fields = ['item__name', 'reason']
    ordering = ['-date']
