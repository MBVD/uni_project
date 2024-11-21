from django.urls import path

from . import views

urlpatterns = [
    path("", views.ShopsController.as_view(), name="index"),
    path("create_fake_data", views.create_fake_data, name = 'create_fake-data'),
    path("features", views.ShopsController.as_view(), name = "features"),
    path("pricing", views.ShopsController.as_view(), name = "pricing"),
    path("about", views.ShopsController.as_view(), name = "about_us"),
]