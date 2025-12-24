from django.db import models

class Tenant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    house_no = models.CharField(max_length=4)
    
    def __str__(self):
        return self.name
    
class Landlord(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    
    
    def __str__(self):
        return self.name

