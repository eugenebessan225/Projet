from django import forms
from pro_it.models import *



class LoginForm(forms.Form):
    email = forms.CharField(label='Email')
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        if email and password:
            utilisateur = Personne.objects.filter(email=email, password=password)
            if len(utilisateur) != 1:
                raise forms.ValidationError('identifiants invalides')
        return cleaned_data





class StagiaireProfilForm(forms.ModelForm):
    nom = forms.CharField(label='', widget=forms.TextInput(
		attrs={
			'class': 'form-control',
			'placeholder': 'Nom *',
		}
	))

    prenom = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Prenom *',
        }
    ))

    email = forms.EmailField(label='', widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'exemple@voila.oui',
        }
    ))



    password = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Mot de passe *',
        }
    ))

    conf_password = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Confirmer mot de passe *',
        }
    ))

    genre = forms.ChoiceField(label='', choices=GENRE, widget=forms.Select(
        attrs={
            'class': 'form-control',
        }
    ))

    filiere_cours = forms.ChoiceField(label='', choices=FILIERE_CHOICES, widget=forms.Select(
        attrs={
            'class': 'form-control',
        }
    ))


    entreprise = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Entreprise acceuillante',
        }
    ))


    projet_titre = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Titre du projet',
        }
    ))

    mots_cles = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Technologies utilisées'
        }
    ))


    description = forms.CharField(label='', widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Brève description du projet',
            'rows': '4',
        }
    ))

    def clean(self):
        cleaned_data = super(StagiaireProfilForm, self).clean()
        password = cleaned_data.get("password")
        conf_password = cleaned_data.get("conf_password")
        if conf_password and password:
            if password != conf_password:
                raise forms.ValidationError('Les mots de passe ne concordent pas ')
        return cleaned_data

    class Meta:
        model = Stagiaire
        exclude = ('avatar', 'date_naissance', 'parrain', 'couverture', 'promo', )


class AineProfilForm(forms.ModelForm):

    nom = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Nom *',
        }
    ))

    prenom = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Prenom *',
        }
    ))

    email = forms.EmailField(label='', widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'exemple@voila.oui',
        }
    ))

    password = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Mot de passe *',
        }
    ))

    conf_password = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Confirmer mot de passe *',
        }
    ))

    genre = forms.ChoiceField(label='', choices=GENRE, widget=forms.Select(
        attrs={
            'class': 'form-control',
        }
    ))

    filiere_faite = forms.ChoiceField(label='', choices=FILIERE_AINE, widget=forms.Select(
        attrs={
            'class': 'form-control',
        }
    ))

    niveau = forms.ChoiceField(label='', choices=STATUT_CHOICES, widget=forms.Select(
        attrs={
            'class': 'form-control',
        }
    ))

    entreprise = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Entreprise où vous êtes embauchés ou avez fait le stage',
        }
    ))

    mots_cles = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Technologies utilisées'
        }
    ))

    def clean(self):
        cleaned_data = super(AineProfilForm, self).clean()
        password = cleaned_data.get("password")
        conf_password = cleaned_data.get("conf_password")
        if conf_password and password:
            if password != conf_password:
                raise forms.ValidationError('Les mots de passe ne concordent pas ')
        return cleaned_data

    class Meta:
        model = Aine
        exclude = ('avatar', 'date_naissance', 'couverture', 'promo',)



class ActuForm(forms.ModelForm):
    class Meta:
        model = Publication
        exclude = ('nbre_jaime', 'nbre_com',)


