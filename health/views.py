from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from .models import HealthRecord
from .serializers import HealthRecordSerializer


class HealthRecordViewSet(viewsets.ModelViewSet):
    serializer_class = HealthRecordSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['description', 'medication', 'veterinarian']
    ordering_fields = ['date', 'record_type']

    def get_queryset(self):
        qs = HealthRecord.objects.filter(owner=self.request.user).select_related('animal')
        animal_id = self.request.query_params.get('animal')
        record_type = self.request.query_params.get('type')
        if animal_id:
            qs = qs.filter(animal_id=animal_id)
        if record_type:
            qs = qs.filter(record_type=record_type)
        return qs

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
