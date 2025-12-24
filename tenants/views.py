from rest_framework.viewsets import ModelViewSet
from accounts.permissions import IsLandlord , IsTenant
from .models import Tenant, Landlord
from .serializers import TenantSerializer, LandlordSerializer


class TenantViewSet(ModelViewSet):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
    permission_classes = [IsTenant]
    
class LandlordViewSet(ModelViewSet):
    queryset = Landlord.objects.all()
    serializer_class = LandlordSerializer
    permission_classes = [IsLandlord]
