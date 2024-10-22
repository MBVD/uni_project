from django.db import models
from djmoney.models.fields import MoneyField


class Shop(models.Model):
  name = models.CharField(max_length=200, primary_key=True)
  url = models.CharField(max_length=200)
  rate = models.IntegerField()

  def __str__(self):
    return self.name
  
  
class Product(models.Model):
  name = models.CharField(max_length=200)
  cost = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
  shop = models.ForeignKey(Shop, on_delete=models.CASCADE)