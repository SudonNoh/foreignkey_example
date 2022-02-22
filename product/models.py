# models.py
from enum import unique
from django.db import models

# Create your models here.
class Owner(models.Model):
    
    name = models.CharField(max_length=128, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=128)
    
class Brand(models.Model):
    
    brand_name = models.CharField(max_length=128, unique=True)
    
class Car_Model(models.Model):
    
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=128)

class Car(models.Model):
    
    car_number = models.CharField(max_length=128)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    car_model = models.ForeignKey(Car_Model, on_delete=models.CASCADE)