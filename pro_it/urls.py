from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = "pro_it"

urlpatterns = [
    path('deconnexion', auth_views.LogoutView.as_view(), name='deconnexion'),
    path('inscription', views.inscription, name='inscription'),
    path('acceuil/', views.acceuil, name="acceuil"),
]
