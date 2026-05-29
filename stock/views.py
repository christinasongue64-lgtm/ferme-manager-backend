from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from .models import StockItem, StockMovement
from .serializers import StockItemSerializer, StockMovementSerializer


class StockItemViewSet(viewsets.ModelViewSet):
    serializer_class = StockItemSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'supplier']
    ordering_fields = ['name', 'quantity', 'category']

    def get_queryset(self):
        qs = StockItem.objects.filter(owner=self.request.user)
        category = self.request.query_params.get('category')
        low_stock = self.request.query_params.get('low_stock')
        if category:
            qs = qs.filter(category=category)
        if low_stock == 'true':
            from django.db.models import F
            qs = qs.filter(quantity__lte=F('min_quantity'))
        return qs

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class StockMovementViewSet(viewsets.ModelViewSet):
    serializer_class = StockMovementSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = StockMovement.objects.filter(owner=self.request.user).select_related('item')
        item_id = self.request.query_params.get('item')
        if item_id:
            qs = qs.filter(item_id=item_id)
        return qs

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
