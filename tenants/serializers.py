from rest_framework import serializers
from .models import Tenant, Landlord

class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = (            
            'name',
            'email',
            'phone',
        )
       
        
class LandlordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Landlord
        fields = (            
            'name',
            'email',
            'phone',
        )