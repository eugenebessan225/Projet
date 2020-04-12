from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from .forms import StagiaireProfilForm, AineProfilForm, ProjetForm, UserRegistrationForm
from .models import Stagiaire, Aine, Projet


def acceuil(request):
    return render(request, 'pro_it/acceuil.html')


@login_required
def welcome(request):
    return render(request, 'pro_it/welcome.html')


def inscription(request):
    if request.POST and 'profileType' in request.POST:
        user_stagiaire_Form = UserRegistrationForm(prefix='st')
        user_aine_Form = UserRegistrationForm(prefix='aine')
        stagiaireForm = StagiaireProfilForm(prefix="st")
        projetForm = ProjetForm(prefix="st")
        aineForm = AineProfilForm(prefix="ai")
        if request.POST['profileType'] == 'stagiaire':
            stagiaireForm = StagiaireProfilForm(
                request.POST, request.FILES, prefix="st")
            user_stagiaire_Form = UserRegistrationForm(
                request.POST, prefix="st")
            projetForm = ProjetForm(request.POST, prefix="st")
            if stagiaireForm.is_valid() and user_stagiaire_Form.is_valid() and projetForm.is_valid():
                user = user_stagiaire_Form.save()
                projet = projetForm.save()
                nouveau_stagiaire = stagiaireForm.save(commit=False)
                nouveau_stagiaire.projet = projet
                nouveau_stagiaire.user = user
                nouveau_stagiaire.save()
                return redirect('connexion')
        elif request.POST['profileType'] == 'aine':
            aineForm = AineProfilForm(
                request.POST, request.FILES, prefix="ai")
            user_aine_Form = UserRegistrationForm(request.POST, prefix="aine")
            if aineForm.is_valid() and user_aine_Form.is_valid():
                user = user_aine_Form.save()
                aine = aineForm.save(commit=False)
                aine.user = user
                aine.save()
                return redirect('connexion')
        return render(request, 'inscription.html', {'stagiaireForm': stagiaireForm, 'aineForm': aineForm, 'user_stagiaire_Form': user_stagiaire_Form, 'user_aine_Form': user_aine_Form, 'projetForm': projetForm})
    else:
        user_stagiaire_Form = UserRegistrationForm(prefix='st')
        user_aine_Form = UserRegistrationForm(prefix='aine')
        stagiaireForm = StagiaireProfilForm(prefix="st")
        projetForm = ProjetForm(prefix="st")
        aineForm = AineProfilForm(prefix="ai")
        return render(request, 'inscription.html', {'stagiaireForm': stagiaireForm, 'aineForm': aineForm, 'user_stagiaire_Form': user_stagiaire_Form, 'user_aine_Form': user_aine_Form, 'projetForm': projetForm})
