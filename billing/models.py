from django.db import models
from tenants.models import Tenant
from django.utils import timezone


class Building(models.Model):
    """
    Optional 
    """
    name = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name


class Rent(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('PARTIAL', 'Partially Paid'),
        ('PAID', 'Paid'),
        ('OVERDUE', 'Overdue'),
    )

    tenant = models.ForeignKey(
        Tenant,
        on_delete=models.CASCADE,
        related_name='rents'
    )
    building = models.ForeignKey(
        Building,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    period = models.CharField(max_length=7)  # YYYY-MM
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='PENDING'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def is_overdue(self):
        return self.due_date < timezone.now().date() and self.status != 'PAID'

    def __str__(self):
        return f"{self.tenant} - {self.period}"


class Payment(models.Model):
    PAYMENT_METHODS = (
        ('CASH', 'Cash'),
        ('BANK', 'Bank Transfer'),
        ('MOBILE', 'Mobile Money'),
    )

    rent = models.ForeignKey(
        Rent,
        on_delete=models.CASCADE,
        related_name='payments'
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField(auto_now_add=True)
    method = models.CharField(
        max_length=10,
        choices=PAYMENT_METHODS
    )
    reference = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.rent.tenant} - {self.amount}"


class LateFee(models.Model):
    rent = models.OneToOneField(
        Rent,
        on_delete=models.CASCADE,
        related_name='late_fee'
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    applied_date = models.DateField(auto_now_add=True)
    is_auto_generated = models.BooleanField(default=False)

    def __str__(self):
        return f"Late fee for {self.rent}"
