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


def connexion(request):
    context = {
        'data': request.POST,
        'has_error': False
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('pro_it:acceuil')
        else:
            messages.add_message(request, messages.ERROR,
                                 "Nom d'utilisateur ou mot de passe incorrect")
            context['has_error'] = True

        if context['has_error']:
            return render(request, 'connexion.html', context)

    return render(request, 'connexion.html')


@login_required
def welcome(request):
    return render(request, 'pro_it/welcome.html')


def change_mdp(request, username):
    context = {
        'data': request.POST,
        'has_error': False
    }
    if request.method == 'POST':
        ancien_mdp = request.POST.get('ancien_mdp')
        nouv_mdp = request.POST.get('nouv_mdp')
        nouv_mdp2 = request.POST.get('nouv_mdp2')

        user = User.objects.get(username=username)

        if not user.check_password(ancien_mdp):
            messages.add_message(request, messages.ERROR,
                                 "Mot de passe actuel incorrect")
            context['has_error'] = True

        if nouv_mdp != nouv_mdp2:
            messages.add_message(request, messages.ERROR,
                                 "Les deux mots de passe ne correspondent pas")
            context['has_error'] = True

        if len(nouv_mdp) < 8 or len(nouv_mdp2) < 8:
            messages.add_message(
                request, messages.ERROR, "Le mot de passe doit contenir au moins 8 caractères")
            context['has_error'] = True

        if context['has_error']:
            return render(request, 'change_mdp.html', context)

        user.set_password(nouv_mdp2)
        user.save()
        update_session_auth_hash(request, user)
        messages.add_message(request, messages.SUCCESS,
                             "Mot de passe changé avec succès")
        return redirect('pro_it:connexion')

    return render(request, 'change_mdp.html', context)


def inscription(request):
    if request.POST and 'profileType' in request.POST:
        userForm = UserRegistrationForm()
        stagiaireForm = StagiaireProfilForm(prefix="st")
        projetForm = ProjetForm(prefix="st")
        aineForm = AineProfilForm(prefix="ai")
        if request.POST['profileType'] == 'stagiaire':
            stagiaireForm = StagiaireProfilForm(
                request.POST, request.FILES, prefix="st")
            userForm = UserRegistrationForm(request.POST)
            projetForm = ProjetForm(request.POST, prefix="st")
            if stagiaireForm.is_valid() and userForm.is_valid() and projetForm.is_valid():
                user = userForm.save()
                projet = projetForm.save()
                nouveau_stagiaire = stagiaireForm.save(commit=False)
                nouveau_stagiaire.projet = projet
                nouveau_stagiaire.user = user
                nouveau_stagiaire.save()
                return redirect('pro_it:connexion')
        elif request.POST['profileType'] == 'aine':
            aineForm = AineProfilForm(
                request.POST, request.FILES, prefix="ai")
            userForm = UserRegistrationForm(request.POST)
            if aineForm.is_valid() and userForm.is_valid():
                user = userForm.save()
                aine = aineForm.save(commit=False)
                aine.user = user
                aine.save()
                return redirect('pro_it:connexion')
        return render(request, 'inscription.html', {'stagiaireForm': stagiaireForm, 'aineForm': aineForm, 'userForm': userForm, 'projetForm': projetForm})
    else:
        userForm = UserRegistrationForm()
        stagiaireForm = StagiaireProfilForm(prefix="st")
        projetForm = ProjetForm(prefix="st")
        aineForm = AineProfilForm(prefix="ai")
        return render(request, 'inscription.html', {'stagiaireForm': stagiaireForm, 'aineForm': aineForm, 'userForm': userForm, 'projetForm': projetForm})
