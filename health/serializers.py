from rest_framework import serializers
from .models import HealthRecord
from django.utils import timezone


class HealthRecordSerializer(serializers.ModelSerializer):
    record_type_display = serializers.CharField(source='get_record_type_display', read_only=True)
    animal_name = serializers.CharField(source='animal.identifier', read_only=True)

    class Meta:
        model = HealthRecord
        fields = '__all__'
        read_only_fields = ['owner', 'created_at', 'record_type_display', 'animal_name']

    def validate_date(self, value):
        if value > timezone.now().date():
            raise serializers.ValidationError("La date du soin ne peut pas être dans le futur.")
        return value

    def validate_cost(self, value):
        if value < 0:
            raise serializers.ValidationError("Le coût ne peut pas être négatif.")
        return value

    def validate(self, data):
        date = data.get('date')
        next_date = data.get('next_date')
        if date and next_date and next_date <= date:
            raise serializers.ValidationError({'next_date': "La date de rappel doit être après la date du soin."})
        return data
