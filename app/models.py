from django.db import models 
from djmoney.models.fields import MoneyField
import datetime
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class CustomUser(AbstractUser):
  info = models.TextField(null = True)
  avatar = models.ImageField(null = True, upload_to = "uploads/users/avatars")
  phone_number = PhoneNumberField(verbose_name="Номер телефона", null=True, blank=True)
  birth_date = models.DateTimeField(verbose_name='Дата рождения', null=True, blank=True)
  groups = models.ManyToManyField(
    'auth.Group',
    related_name='groups',
    blank=True,
    help_text='The groups this user belongs to.',
    verbose_name='groups',
  )
  user_permissions = models.ManyToManyField(
    'auth.Permission',
    related_name='permissions',
    blank=True,
    help_text='Specific permissions for this user.',
    verbose_name='user permissions',
  )

  def __str__(self):
    return self.username

class Shop(models.Model):   
  id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
  image = models.ImageField(upload_to ='uploads/shops', null = True) 
  name = models.CharField(max_length=200, unique=True)   
  url = models.CharField(max_length=200)   
  rate = models.IntegerField()  
  is_present = models.BooleanField(default=True)

  def __str__(self):     
    return self.name       
  
  
class Product(models.Model):   
  name = models.CharField(max_length=255)
  description = models.TextField(null = True)   
  cost = MoneyField(max_digits=14, decimal_places=2, default_currency='KZT')
  image = models.ImageField(upload_to ='uploads/products', null = True) 
  shops = models.ManyToManyField(Shop)
  specs = models.JSONField(null = True)
  is_present = models.BooleanField(default=True)


class ProductCost(models.Model):
  cost_on_date = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
  date = models.DateField(default=datetime.date.today)
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  