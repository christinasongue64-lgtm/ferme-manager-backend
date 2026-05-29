from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StockItemViewSet, StockMovementViewSet

router = DefaultRouter()
router.register('items', StockItemViewSet, basename='stock-item')
router.register('movements', StockMovementViewSet, basename='stock-movement')
urlpatterns = [path('', include(router.urls))]
