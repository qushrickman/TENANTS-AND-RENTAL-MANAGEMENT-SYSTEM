from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tenants.views import TenantViewSet, LandlordViewSet
from accounts.views import RegisterView


from billing.views import LateFeeViewSet, PaymentViewSet, RentViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = DefaultRouter()
router.register('tenants', TenantViewSet, basename='tenant')
router.register('rents', RentViewSet, basename='rent')
router.register('payments', PaymentViewSet, basename='payment')
router.register('late-fees', LateFeeViewSet, basename='late-fee')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    
     path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
     path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
     path('api/auth/register/', RegisterView.as_view(), name='register'),
]
