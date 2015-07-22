from django.db import models
from django.utils import timezone
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length = 50)
    manufacturer = models.CharField(max_length = 50)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    description = models.CharField(max_length = 50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
