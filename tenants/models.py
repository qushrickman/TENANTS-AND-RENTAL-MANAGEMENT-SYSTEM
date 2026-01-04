from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class Tenant(models.Model):       
    name = models.CharField(max_length=255),
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    
    
    def __str__(self):
        return self.name
    
class Landlord(models.Model):   
    name = models.CharField(max_length=255),
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    
    
    def __str__(self):
        return self.name

