from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenRefreshView
from users.views import CustomTokenObtainPairView, RegisterView, LogoutView, MeView

admin.site.site_header = "🐄 Ferme Manager — Administration"
admin.site.site_title = "Ferme Manager"
admin.site.index_title = "Tableau de bord administrateur"

urlpatterns = [
    path('admin/', admin.site.urls),
    # Auth
    path('api/auth/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/register/', RegisterView.as_view(), name='register'),
    path('api/auth/logout/', LogoutView.as_view(), name='logout'),
    path('api/auth/me/', MeView.as_view(), name='me'),
    # Apps
    path('api/animals/', include('animals.urls')),
    path('api/health/', include('health.urls')),
    path('api/stock/', include('stock.urls')),
    path('api/sales/', include('sales.urls')),
    path('api/finance/', include('finance.urls')),
    path('api/dashboard/', include('users.dashboard_urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
