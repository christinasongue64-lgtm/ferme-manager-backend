from rest_framework import serializers
from .models import Animal
from django.utils import timezone


class AnimalSerializer(serializers.ModelSerializer):
    animal_type_display = serializers.CharField(source='get_animal_type_display', read_only=True)
    sex_display = serializers.CharField(source='get_sex_display', read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    entry_type_display = serializers.CharField(source='get_entry_type_display', read_only=True)

    class Meta:
        model = Animal
        fields = '__all__'
        read_only_fields = ['owner', 'identifier', 'created_at', 'updated_at',
                            'animal_type_display', 'sex_display', 'status_display', 'entry_type_display']

    def validate_birth_date(self, value):
        if value and value > timezone.now().date():
            raise serializers.ValidationError("La date de naissance ne peut pas être dans le futur.")
        return value

    def validate_entry_date(self, value):
        if value > timezone.now().date():
            raise serializers.ValidationError("La date d'entrée ne peut pas être dans le futur.")
        return value

    def validate_weight(self, value):
        if value is not None and value <= 0:
            raise serializers.ValidationError("Le poids doit être positif.")
        return value
