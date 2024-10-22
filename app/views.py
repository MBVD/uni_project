from django.shortcuts import render
from django.http import HttpResponse 
from .models import *
from django.views import View

# Create your views here

class ShopsController(View):
  def get(self, request):
    shops = Shop.objects.all()
    return render(request, "shops/index.html", {"shops": shops})  
  
  def post(self, request):
    pass