from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tenants.views import TenantViewSet

from billing.views import LateFeeViewSet

router.register(r'late-fees', LateFeeViewSet, basename='late-fee')

router = DefaultRouter()
router.register(r'tenants', TenantViewSet, basename='tenant')

urlpatterns = [
    path('api/', include(router.urls)),
]
