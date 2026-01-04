from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsLandlord , IsTenant
from billing import serializers
from .models import Tenant, Landlord
from django.http import JsonResponse
from .serializers import TenantSerializer, LandlordSerializer


def tenantlist(request):
    tenants = Tenant.objects.all().values('name', 'email', 'phone')
    TenantSerializer(tenants, many=True)
    return JsonResponse(
        {'tenants_data' : serializers.data},
        safe=False
        )
    
    
class TenantViewSet(ModelViewSet):
    serializer_class = TenantSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        profile = user.profile

        # Landlord sees their tenants
        if profile.Role == 'landlord':
            return Tenant.objects.filter(landlord__user=user)

        # Tenant sees only themselves
        if profile.Role == 'tenant':
            return Tenant.objects.filter(user=user)

        return Tenant.objects.none()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
class LandlordViewSet(ModelViewSet):
    serializer_class = LandlordSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Landlord.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)