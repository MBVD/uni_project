from codecs import utf_7_decode
from datetime import datetime
from django import template
from django.urls import reverse


def navigation_panel(request):
    return {"navigation_panel": {"Главная": reverse('index'),
            "Предложения": reverse('features'),
            "Цены": reverse('pricing'),
            "О нас": reverse('about_us')}}