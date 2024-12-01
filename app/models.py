from django.db import models 
from djmoney.models.fields import MoneyField
import datetime

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
  name = models.CharField(max_length=200)   
  cost = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
  image = models.ImageField(upload_to ='uploads/products', null = True) 
  shops = models.ManyToManyField(Shop)
  is_present = models.BooleanField(default=True)


class ProductCost(models.Model):
  cost_on_date = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
  date = models.DateField(default=datetime.date.today)
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  