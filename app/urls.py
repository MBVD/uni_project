from django.urls import path

from . import views

urlpatterns = [
    path("", views.ShopsController.as_view(), name="home"),
    path("create_fake_data", views.create_fake_data, name = 'create_fake-data'),
    path("features", views.ShopsController.as_view(), name = "features"),
    path("pricing", views.ShopsController.as_view(), name = "pricing"),
    path("about", views.ShopsController.as_view(), name = "about_us"),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.LogoutUser.as_view(), name='logout'),
]