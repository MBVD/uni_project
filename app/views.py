from django.shortcuts import render
from django.http import HttpResponse 
from .models import *
from django.views import View
from django.shortcuts import redirect
from django.views.generic import TemplateView
from .forms import SearchForm
from faker import Faker
import faker_commerce

# Create your views here

def create_fake_data(request):
  fake = Faker()
  fake.add_provider(faker_commerce.Provider)
  if "delete" in request.GET.keys() and request.GET["delete"] == "1":
    shops = Shop.objects.all()
    shops.delete()
  if "create" in request.GET.keys() and request.GET["create"] == "1":
    for _ in range(100):
      shop = Shop.objects.create(name = fake.company(),
                          url = fake.address(),
                          rate = fake.pyint(),
                          is_present = fake.pybool())
      product = Product.objects.create(name = fake.ecommerce_name(),
                                        cost = fake.ecommerce_price(),
                                        shop = shop,
                                        is_present = True)
      product_cost = ProductCost.objects.create(cost_on_date = fake.ecommerce_price(),
                                                date = fake.date(),
                                                product = product)

  return redirect('index')


class ShopsController(TemplateView):
  template_name  = "shops/index.html"
  extra_context = {
    "title": 'Домашняя страница'  
  }

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    form = SearchForm(self.request.GET)
    if form.is_valid():
      context["shops"] = Shop.objects.filter(name__icontains=form["text"].value())
    else:
      context["shops"] = Shop.objects.all()
    context["form"] = form
    # context["shops"] = Shop.objects.all()
    return context