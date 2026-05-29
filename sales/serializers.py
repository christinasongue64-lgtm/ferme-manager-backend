from rest_framework import serializers
from .models import Sale
from django.utils import timezone


class SaleSerializer(serializers.ModelSerializer):
    total_price = serializers.DecimalField(max_digits=14, decimal_places=2, read_only=True)
    animal_identifier = serializers.CharField(source='animal.identifier', read_only=True, allow_null=True)

    class Meta:
        model = Sale
        fields = '__all__'
        read_only_fields = ['owner', 'created_at', 'total_price', 'animal_identifier']

    def validate_date(self, value):
        if value > timezone.now().date():
            raise serializers.ValidationError("La date de vente ne peut pas être dans le futur.")
        return value

    def validate_unit_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Le prix doit être positif.")
        return value

    def validate_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError("La quantité doit être positive.")
        return value

    def validate(self, data):
        # If animal sold, update its status
        animal = data.get('animal')
        if animal and animal.status != 'alive':
            raise serializers.ValidationError({'animal': "Cet animal n'est plus disponible à la vente."})
        return data

    def create(self, validated_data):
        sale = super().create(validated_data)
        # Mark animal as sold if linked
        if sale.animal:
            sale.animal.status = 'sold'
            sale.animal.save()
        return sale
