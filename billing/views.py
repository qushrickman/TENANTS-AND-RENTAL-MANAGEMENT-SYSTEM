from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Payment
from .serializers import PaymentSerializer
from accounts.permissions import IsLandlord, IsTenant

class PaymentViewSet(ModelViewSet):
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        # Landlord sees all payments
        if user.profile.role == 'LANDLORD':
            return Payment.objects.all()

        # Tenant sees only their own payments
        if user.profile.role == 'TENANT':
            return Payment.objects.filter(rent__tenant__user=user)

        return Payment.objects.none()

    def perform_create(self, serializer):
        # Tenant can create payment for their rent only
        user = self.request.user
        if user.profile.role == 'TENANT':
            serializer.save()
        else:
            # Optionally raise permission denied
            serializer.save()
