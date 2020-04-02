from django.db import models
from datetime import datetime
from datetime import date

FILIERE_CHOICES = [
	('', 'Choisissez votre filière'),
	('SRIT','SRIT'),
	('TWIN','TWIN'),
	('SIGL','SIGL'),
	('RTEL','RTEL')
]

FILIERE_AINE = [
	('', 'Choisissez votre filière'),
	('SIGL', 'SIGL'),
	('SITW', 'SITW'),
	('RTEL', 'RTEL'),
	('MDSI', 'MDSI'),
	('MBDS', 'MBDS')
]

STATUT_CHOICES = [
	('', 'Votre Statut'),
	('PROFESSIONNEL','PROFESSIONNEL'),
	('ETUDIANT','ETUDIANT', )
]

GENRE=[
	('HOMME', 'HOMME'),
	('FEMME', 'FEMME')
]

PROMO_CHOICES = [
	('IT 01', 'IT 01'),
	('IT 02', 'IT 02'),
	('IT 03', 'IT 03'),
	('IT 04', 'IT 04'),
	('IT 05', 'IT 05'),
	('IT 06', 'IT 06'),
]

class Personne(models.Model):
	"""Représente les parties prenantes sur ce site"""

	nom = models.CharField(max_length = 50, null = True)
	prenom = models.CharField(max_length = 50, null = True)
	email = models.CharField(max_length = 100, null = True)
	genre = models.CharField(max_length=10, null=True, choices=GENRE)
	promo = models.CharField(max_length=10, null=True, choices=PROMO_CHOICES)
	date_naissance = models.DateField(null=True)
	avatar = models.ImageField(upload_to='avatar', default='avatar/avatar.jpg', blank=True)
	couverture = models.ImageField(upload_to='couverture', default='couverture/avatar.jpg', blank=True)
	entreprise = models.CharField(max_length = 100, null = True)
	mots_cles = models.CharField(max_length = 200, null = True, verbose_name = "Technologies utilisées")
	password = models.CharField(max_length  = 200, null = True, verbose_name = "Mot de passe")
	person_type = 'generic'




class Aine(Personne):
	niveau = models.CharField(max_length = 50, null = True, verbose_name = "Statut", choices = STATUT_CHOICES)
	filiere_faite = models.CharField(max_length = 50, null = True, choices = FILIERE_AINE, verbose_name = "Filière faite ou en cours")
	person_type = 'Aine'


class Stagiaire(Personne):
	projet_titre = models.CharField(max_length=100, null=True, verbose_name = "Titre du projet")
	filiere_cours = models.CharField(max_length=50, null=True, choices=FILIERE_CHOICES, verbose_name="Filière")
	description = models.CharField(max_length=200, null=True, verbose_name = "Brève description")
	parrain = models.ManyToManyField(Aine, related_name = "filieuls")
	person_type = 'Stagiaire'



class Photo_actualite(models.Model):
	#auteur = models.ForeignKey(Personne, related_name="publications", on_delete=models.CASCADE)
	image = models.ImageField(upload_to='actualité', null=True, blank=True)
	description = models.CharField(max_length=500, null=True)
	#publication_date = models.DateTimeField(default=datetime.now().time(), blank=True, null=True)
	nbre_jaime = models.IntegerField(default=0)
	nbre_com = models.IntegerField(default=0)



