from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tenants.views import TenantViewSet, LandlordViewSet

from billing.views import LateFeeViewSet, PaymentViewSet, RentViewSet


router = DefaultRouter()
router.register('tenants', TenantViewSet, basename='tenant')
router.register('rents', RentViewSet, basename='rent')
router.register('payments', PaymentViewSet, basename='payment')
router.register('late-fees', LateFeeViewSet, basename='late-fee')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
