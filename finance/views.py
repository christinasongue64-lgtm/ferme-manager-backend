from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from .models import Expense
from .serializers import ExpenseSerializer


class ExpenseViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['description', 'supplier']
    ordering_fields = ['date', 'amount', 'category']

    def get_queryset(self):
        qs = Expense.objects.filter(owner=self.request.user)
        category = self.request.query_params.get('category')
        month = self.request.query_params.get('month')
        year = self.request.query_params.get('year')
        if category:
            qs = qs.filter(category=category)
        if month:
            qs = qs.filter(date__month=month)
        if year:
            qs = qs.filter(date__year=year)
        return qs

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
