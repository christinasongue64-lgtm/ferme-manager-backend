from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from datetime import timedelta


class DashboardStatsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        now = timezone.now()
        start_of_month = now.replace(day=1, hour=0, minute=0, second=0)

        from animals.models import Animal
        from stock.models import StockItem
        from sales.models import Sale
        from finance.models import Expense
        from health.models import HealthRecord

        # Animals
        total_animals = Animal.objects.filter(owner=user, status='alive').count()
        animals_by_type = list(
            Animal.objects.filter(owner=user, status='alive')
            .values('animal_type')
            .annotate(count=__import__('django.db.models', fromlist=['Count']).Count('id'))
        )

        # Stock alerts (quantity < min_quantity)
        low_stock = StockItem.objects.filter(owner=user, quantity__lte=__import__('django.db.models', fromlist=['F']).F('min_quantity')).count()

        # Sales this month
        monthly_sales = Sale.objects.filter(
            owner=user,
            date__gte=start_of_month
        )
        monthly_revenue = sum(s.total_price for s in monthly_sales)
        monthly_sales_count = monthly_sales.count()

        # Expenses this month
        monthly_expenses = Expense.objects.filter(
            owner=user,
            date__gte=start_of_month
        )
        monthly_expense_total = sum(e.amount for e in monthly_expenses)

        # Upcoming vaccines (next 7 days)
        upcoming_vaccines = HealthRecord.objects.filter(
            owner=user,
            record_type='vaccination',
            next_date__gte=now.date(),
            next_date__lte=(now + timedelta(days=7)).date()
        ).count()

        return Response({
            'total_animals': total_animals,
            'animals_by_type': animals_by_type,
            'low_stock_count': low_stock,
            'monthly_revenue': float(monthly_revenue),
            'monthly_expense_total': float(monthly_expense_total),
            'monthly_profit': float(monthly_revenue - monthly_expense_total),
            'monthly_sales_count': monthly_sales_count,
            'upcoming_vaccines': upcoming_vaccines,
        })
