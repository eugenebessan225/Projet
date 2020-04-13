from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from . import liste_choices

<<<<<<< HEAD

class Groupe(models.Model):
	nom = models.CharField(max_length=50, null=True)
	description = models.CharField(max_length=100, null=True)


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
	groupe = models.ForeignKey(Groupe, related_name="membres",null=True, on_delete=models.CASCADE)
	person_type = 'generic'
=======

class Technologie(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom
>>>>>>> 8045004f51eef1fb9f01daab3dd124e763202855


class Personne(models.Model):
    """Représente les parties prenantes sur ce site"""
    person_type = 'generic'
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='personne')
    genre = models.CharField(max_length=10, choices=liste_choices.GENRE)
    promotion = models.CharField(
        max_length=10, choices=liste_choices.PROMO_CHOICES)
    date_naissance = models.DateField('date de naissance')
    numero_telephone = models.CharField('numéro de téléphone', max_length=20)
    avatar = models.ImageField(
        upload_to='personne/avatar', default='personne/avatar/avatar.jpg')
    couverture = models.ImageField(
        upload_to='personne/couverture', default='personne/couverture/avatar.jpg')
    entreprise = models.CharField(max_length=100)
    technologie = models.ManyToManyField(
        Technologie, verbose_name="technologies utilisées")
    statut = models.CharField(
        max_length=50, choices=liste_choices.STATUT_CHOICES)
    filiere = models.CharField(
        'filière', max_length=50, choices=liste_choices.FILIERE_CHOICES)
    amis = models.ManyToManyField('self')

    def __str__(self):
        return self.user.last_name + " " + self.user.first_name


class Aine(Personne):
    person_type = 'aine'


class Projet(models.Model):
    titre_projet = models.CharField('thème du ptojet', max_length=100)
    description = models.CharField('description du projet', max_length=200)

    def __str__(self):
        return self.titre_projet[:19] + "..."


class Stagiaire(Personne):
    person_type = 'stagiaire'
    projet = models.OneToOneField(
        Projet, on_delete=models.CASCADE, related_name="stagiaire")
    parrain = models.ManyToManyField(
        Aine, related_name="filieuls", default=None, blank=True)


class Publication(models.Model):
    auteur = models.ForeignKey(
        Personne, related_name="publications", on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    date = models.DateTimeField(
        default=timezone.now)
    nbre_jaime = models.IntegerField(default=0)
    nbre_comment = models.IntegerField(default=0)

    def __str__(self):
        return self.description[:19] + "..."


class Document(Publication):
    contenu = models.FileField(upload_to='publication/documents/')


class Image(Publication):
    contenu = models.ImageField(upload_to='publication/images/')


class Texte(Publication):
    contenu = models.TextField()


class Video(Publication):
    contenu = models.FileField(upload_to='publication/videos/')


class Commentaire(models.Model):
    auteur = models.ForeignKey(
        Personne, related_name='commentaires', on_delete=models.CASCADE)
    contenu = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    publication = models.ForeignKey(
        Publication, related_name='commentaires', on_delete=models.CASCADE)

    def __str__(self):
        return self.auteur

# explication


class Groupe(models.Model):
    nom = models.CharField(max_length=100)
    membres = models.ManyToManyField(Personne)

<<<<<<< HEAD


class Notification(models.Model):
	proprio = models.ForeignKey(Personne, related_name="Notifications", on_delete=models.CASCADE)
	objet = models.CharField(max_length=50, null=True, blank=True)
	contenu = models.CharField(max_length=100, null=True)


class Messages(models.Model):
	auteur = models.ForeignKey(Personne, related_name="messages_envoyés", on_delete=models.CASCADE)
	destinateur = models.ManyToManyField(Personne, related_name="messages_reçus")
	contenu = models.CharField(max_length=1000, null=True)
	date_publication = models.DateTimeField(null=True, default=datetime.now())



class Publication(models.Model):
	auteur = models.ForeignKey(Personne, related_name="publications", on_delete=models.CASCADE)
	image = models.ImageField(upload_to='actualité', null=True, blank=True)
	description = models.CharField(max_length=500, null=True)
	publication_date = models.DateTimeField(default=datetime.now().time(), blank=True, null=True)
	nbre_com = models.IntegerField(default=0)


class Commentaire(models.Model):
	auteur = models.ForeignKey(Personne, related_name="commentaires_faits", on_delete=models.CASCADE)
	publication = models.ForeignKey(Publication, related_name="commentaires_ecrits", on_delete=models.CASCADE)


=======
    def __str__(self):
        return self.nom


class Notification(models.Model):
    receveur = models.ManyToManyField(Personne, related_name='notifications')
    objet = models.CharField(max_length=50)
    contenu = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
>>>>>>> 8045004f51eef1fb9f01daab3dd124e763202855

    def __str__(self):
        return self.objet
