from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = "pro_it"

urlpatterns = [
    path('', views.connexion, name='connexion'),
    path('deconnexion', auth_views.LogoutView.as_view(), name='deconnexion'),
    path('inscription', views.inscription, name='inscription'),
    path('acceuil/', views.acceuil, name="acceuil"),
    path('changer-mot-de-passe/<str:username>/',
         views.change_mdp, name='change_mdp'),
]
