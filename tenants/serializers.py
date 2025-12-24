from rest_framework import serializers
from .models import Tenant, Landlord

class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = '__all__'
        read_only_fields = ('user',)
        
class LandlordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Landlord
        fields = '__all__'
        read_only_fields = ('user',)
