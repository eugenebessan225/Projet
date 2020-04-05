from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = "pro_it"

urlpatterns = [
    path('', views.acceuil, name="acceuil"),
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('welcome', views.welcome, name='welcome'),
]
