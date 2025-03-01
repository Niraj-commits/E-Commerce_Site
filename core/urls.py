from django.urls import path,include
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register_buyer/',RegisterBuyer,name="register_buyer"),
    path('register_seller/',RegisterSeller,name="register_seller"),
    path('login/',CustomLogin,name="login"),
    path('logout/',logout,name="logout")
]
