from django.urls import path

from . import views

urlpatterns = [
    path("", views.ShopsController.as_view(), name="home"),
    path("shops/<int:id>/", views.ShopsController.as_view(), name = "shop"),
    path("products/<int:id>", views.ProductsController.as_view(), name = "product"),
    path("create_fake_data", views.create_fake_data, name = 'create_fake-data'),
    path("features", views.ShopsController.as_view(), name = "features"),
    path("pricing", views.PriceController.as_view(), name = "pricing"),
    path("about", views.AboutController.as_view(), name = "about_us"),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.LogoutUser.as_view(), name='logout'),
    path('cabinet/', views.CabinetController.as_view(), name = 'cabinet'),
]