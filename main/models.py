from django.db import models
from django.contrib.auth.models import User
import random
# Create your models here.
class Car(models.Model):
    brand = models.CharField('Brand nomi',max_length=150)
    model = models.CharField('Modeli',max_length=150)
    color = models.CharField('Rangi',max_length=100)
    number = models.CharField('Mashina raqami',max_length=150)

    def __str__(self):
        return self.brand 
class Driver(models.Model):
    first_name = models.CharField('Xaydovchi ismi',max_length=150)
    last_name = models.CharField('Xaydovchi Familiyasi',max_length=150)
    car = models.CharField('Mashina',max_length=150)
    def __str__(self):
        return self.first_name