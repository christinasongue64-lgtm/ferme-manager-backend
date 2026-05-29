from rest_framework import serializers
from .models import StockItem, StockMovement


class StockItemSerializer(serializers.ModelSerializer):
    category_display = serializers.CharField(source='get_category_display', read_only=True)
    is_low = serializers.BooleanField(read_only=True)
    total_value = serializers.DecimalField(max_digits=12, decimal_places=2, read_only=True)

    class Meta:
        model = StockItem
        fields = '__all__'
        read_only_fields = ['owner', 'updated_at', 'category_display', 'is_low', 'total_value']

    def validate_quantity(self, value):
        if value < 0:
            raise serializers.ValidationError("La quantité ne peut pas être négative.")
        return value

    def validate_min_quantity(self, value):
        if value < 0:
            raise serializers.ValidationError("Le seuil d'alerte ne peut pas être négatif.")
        return value

    def validate_unit_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Le prix ne peut pas être négatif.")
        return value


class StockMovementSerializer(serializers.ModelSerializer):
    movement_type_display = serializers.CharField(source='get_movement_type_display', read_only=True)
    item_name = serializers.CharField(source='item.name', read_only=True)

    class Meta:
        model = StockMovement
        fields = '__all__'
        read_only_fields = ['owner', 'created_at', 'movement_type_display', 'item_name']

    def validate_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError("La quantité doit être positive.")
        return value

    def validate(self, data):
        # Check stock doesn't go negative on output
        if data.get('movement_type') == 'out':
            item = data.get('item')
            qty = data.get('quantity', 0)
            if item and item.quantity < qty:
                raise serializers.ValidationError(
                    {'quantity': f"Stock insuffisant. Disponible : {item.quantity} {item.unit}"}
                )
        return data

    def create(self, validated_data):
        movement = super().create(validated_data)
        item = movement.item
        if movement.movement_type == 'in':
            item.quantity += movement.quantity
        else:
            item.quantity -= movement.quantity
        item.save()
        return movement
