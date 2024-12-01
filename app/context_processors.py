from codecs import utf_7_decode
from datetime import datetime
from django import template
from django.urls import reverse


def navigation_panel(request):
    return {"navigation_panel": {"Главная": reverse('home'),
            "Предложения": reverse('features'),
            "Цены": reverse('pricing'),
            "О нас": reverse('about_us')}}


def current_year(request):
    return {"current_year": datetime.now().year}