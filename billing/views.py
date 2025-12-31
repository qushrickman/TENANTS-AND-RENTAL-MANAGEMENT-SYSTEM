from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Payment, LateFee, Rent
from .serializers import PaymentSerializer
from accounts.permissions import IsLandlord, IsTenant

class PaymentViewSet(ModelViewSet):
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        
        if user.profile.role == 'LANDLORD':
            return Payment.objects.all()

       
        if user.profile.role == 'TENANT':
            return Payment.objects.filter(rent__tenant__user=user)

        return Payment.objects.none()

    def perform_create(self, serializer):
       
        user = self.request.user
        if user.profile.role == 'TENANT':
            serializer.save()
        else:
            
            serializer.save()

class LateFeeViewSet(ModelViewSet):
    queryset = LateFee.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated, IsLandlord]
    
class RentViewSet(ModelViewSet):
    queryset = Rent.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated, IsLandlord]
    