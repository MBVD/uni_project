from django.urls import path

from . import views

urlpatterns = [
    path("", views.ShopsController.as_view(), name="index"),
    path("features", views.ShopsController.as_view() ,name="features"),
    path("pricing", views.ShopsController.as_view(), name = "pricing"),
    path("about", views.ShopsController.as_view(), name = "about_us"),
]