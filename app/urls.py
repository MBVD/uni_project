from django.urls import path

from . import views

urlpatterns = [
    path("", views.ShopsController.as_view(), name="index"),
]