from rest_framework import serializers
from .models import Rent, Payment, LateFee

class RentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rent
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
        read_only_fields = ('payment_date',)

    def create(self, validated_data):
        payment = super().create(validated_data)
        rent = payment.rent

        total_paid = sum(p.amount for p in rent.payments.all())
        if total_paid >= rent.amount:
            rent.status = 'PAID'
        else:
            rent.status = 'PARTIAL'
        rent.save()

        return payment
    
class LateFeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LateFee
        fields = '__all__'
