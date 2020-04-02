from django.shortcuts import render, redirect
from pro_it.forms import *
from django.contrib import messages



def index(request):
    return render(request, 'pro_it/index.html')


def register(request):

    if len(request.POST) > 0 and 'profileType' in request.POST:
        AineForm = AineProfilForm(request.POST, prefix="a")
        StagiaireForm = StagiaireProfilForm(request.POST, prefix="s")
        if request.POST['profileType'] == 'aine':
            print("je sui un aine")
            AineForm = AineProfilForm(request.POST, prefix="a")
            print("form aine ", AineForm)
            if AineForm.is_valid():
                AineForm.save()
                return redirect('./acceuil')
            else:
                nonvalide = True
                return render(request, 'pro_it/register.html', locals())

        elif request.POST['profileType'] == 'stagiaire':
            StagiaireForm = StagiaireProfilForm(request.POST, prefix="s")
            print("formulaire", StagiaireForm.errors)
            if StagiaireForm.is_valid():
                StagiaireForm.save()
                return redirect('./acceuil')

            else:
                nonvalide = True
                return render(request, 'pro_it/register.html', locals())
    else:
        AineForm = AineProfilForm(prefix="a")
        StagiaireForm = StagiaireProfilForm(prefix="s")

        return render(request, 'pro_it/register.html', locals())




def login(request):

    if len(request.POST) > 0:
        form = LoginForm(request.POST)
        if form.is_valid():
            utilisateur_email = form.cleaned_data['email']
            utilisateur = Personne.objects.get(email=utilisateur_email)
            request.session['utilisateur_id'] = utilisateur.id

            return redirect('./acceuil')

        else:
            utilisateur = "not"
            return render(request, 'pro_it/login.html', locals())
    else:
        form = LoginForm()
        return render(request, 'pro_it/login.html', locals())




def get_utilisateur(request):
    if 'utilisateur_id' in request.session:
        utilisateur_id = request.session['utilisateur_id']
        if len(Stagiaire.objects.filter(id=utilisateur_id)) == 1:
            return Stagiaire.objects.get(id=utilisateur_id)
        elif len(Aine.objects.filter(id=utilisateur_id)) == 1:
            return Aine.objects.get(id=utilisateur_id)
        else:
            return None
    else:
        return None



def publication():
    publications = Photo_actualite.objects.all()
    return publications


def acceuil(request):
    utilisateur = get_utilisateur(request)
    if utilisateur:
        publications = publication()
        return render(request, 'pro_it/acceuil.html', locals())
    else:
        return redirect('./login')


def publier(request):
    utilisateur = get_utilisateur(request)

    if utilisateur:
        if len(request.POST) > 0:
            form = ActuForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                publications = publication()
                return render(request, 'pro_it/acceuil.html', locals())
            else:
                return render(request, 'pro_it/publier.html', {'form': form})
        else:
            form = ActuForm()
            return render(request, 'pro_it/publier.html', {'form': form})
    else:
        return redirect('./login')








