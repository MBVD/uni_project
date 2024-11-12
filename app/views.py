from django.shortcuts import render
from django.http import HttpResponse 
from .models import *
from django.views import View
from django.views.generic import TemplateView
from .forms import SearchForm

# Create your views here

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