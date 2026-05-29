from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from .models import Animal
from .serializers import AnimalSerializer


class AnimalViewSet(viewsets.ModelViewSet):
    serializer_class = AnimalSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['identifier', 'name', 'breed', 'animal_type']
    ordering_fields = ['entry_date', 'animal_type', 'status']

    def get_queryset(self):
        qs = Animal.objects.filter(owner=self.request.user)
        animal_type = self.request.query_params.get('type')
        status = self.request.query_params.get('status')
        if animal_type:
            qs = qs.filter(animal_type=animal_type)
        if status:
            qs = qs.filter(status=status)
        return qs

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
