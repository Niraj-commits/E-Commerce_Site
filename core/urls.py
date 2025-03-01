from django.urls import path,include
from .views import *
from django.contrib.auth import views as auth_views
from .forms import LoginForm

urlpatterns = [
    path('signup/',signup,name="signup"),
    path('login/',auth_views.LoginView.as_view(template_name = 'authentication/login.html',authentication_form=LoginForm),name='login'),
    path('logout/',logout,name="logout")
]
