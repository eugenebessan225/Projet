from django import forms
from .models import Aine, Stagiaire, Projet
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    last_name = forms.CharField(max_length=25, label="Nom")
    first_name = forms.CharField(max_length=25, label="Prénom")

    class Meta:
        model = User
        fields = ('username', 'email', 'last_name',
                  'first_name', 'password1', 'password2')


class StagiaireProfilForm(forms.ModelForm):
    class Meta:
        model = Stagiaire
        exclude = ('amis', 'parrain', 'user', 'projet')


class ProjetForm(forms.ModelForm):
    class Meta:
        model = Projet
        fields = "__all__"


class AineProfilForm(forms.ModelForm):
    class Meta:
        model = Aine
        exclude = ('amis', 'user')
