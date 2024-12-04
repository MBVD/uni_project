from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse 
from .models import *
from django.views import View
from django.shortcuts import redirect
from django.views.generic import TemplateView
from .forms import *
from faker import Faker
import faker_commerce
from django.views.generic import *
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.core.paginator import Paginator
from django.db.models import Q
import random



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
      for __ in range(random.randint(0, 10)):
        product = Product.objects.create(name = fake.ecommerce_name(),
                                          cost = fake.ecommerce_price(),
                                          is_present = True)
        shop.product_set.add(product)
      product_cost = ProductCost.objects.create(cost_on_date = fake.ecommerce_price(),
                                                date = fake.date(),
                                                product = product)

  return redirect('home')


class ShopsController(TemplateView):
  template_name  = "app/shops/index.html"
  extra_context = {
    "title": 'Домашняя страница'  
  }

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    search_form = SearchForm(self.request.GET)
    page_number = self.request.GET.get("page")
    id = self.kwargs.get("id")
    print("jsdklfjaslkfjaskldfjkaskl")
    print(id)
    if id:
      shop = get_object_or_404(Shop, id=id)
      paginator = Paginator(shop.product_set.all(), 3)
      page_obj = paginator.get_page(page_number)
      self.template_name = "app/shops/show.html"
      context["shop"] = shop
      context["page_obj"] = page_obj
      return context
    if search_form.is_valid():
      search_text = search_form.cleaned_data.get("text", "")
      shops = Shop.objects.filter(Q(name__icontains = search_text) | Q(product__name__icontains = search_text))
    else:
      shops = Shop.objects.all()
    paginator = Paginator(shops, 21)
    context["page_obj"] = paginator.get_page(page_number)
    context["search_form"] = search_form
    # context["shops"] = Shop.objects.all()
    return context
  
class ProductsController(TemplateView):
  template_name = "app/product/show.html"
  extra_context = {
    "title": 'Магазин'  
  }

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    id = self.kwargs.get("id")
    product = get_object_or_404(Product, id=id)
    context["product"] = product

    return context



class AboutController(TemplateView):
  template_name = "app/about/about.html"
  extra_context = {
    "title": "О нас"
  }

class PriceController(TemplateView):
  template_name = "app/pricing/pricing.html"
  extra_context = {
    "title": "Цены"
  }

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    return context

class RegisterUser(CreateView):
  form_class = RegisterUserForm
  template_name = 'app/login.html'
  success_url = reverse_lazy('home')
  extra_context = {
      'title': 'Регистрация'
  }

  def form_valid(self, form):
    user = form.save()
    login(self.request, user)
    return redirect('home')


class LoginUser(LoginView):
  form_class = LoginUserForm
  template_name = 'app/login.html'
  extra_context = {
    'title': 'Авторизация'
  }

  def get_success_url(self):
    return reverse_lazy('home')

class LogoutUser(LogoutView):
  template_name = 'logged_out.html'
  next_page = 'home'

class CabinetController(FormView):
  template_name = 'app/cabinet/index.html'
  form_class = CustomUserChangeForm
  success_url = reverse_lazy("home")
  extra_context = {
    "title": "Личный кабинет"
  }

  def get_form_kwargs(self):
    kwargs = super().get_form_kwargs()
    kwargs['instance'] = self.request.user
    return kwargs

  def form_valid(self, form):
    if form.is_valid:
      form.save()
    else:
      print(form.errors)
      print("jsdkdfjasf")
    return super().form_valid(form)

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)

    return context