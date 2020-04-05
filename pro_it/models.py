from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from . import liste_choices


class Technologie(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


class Personne(models.Model):
    """Représente les parties prenantes sur ce site"""
    person_type = 'generic'
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='personne')
    genre = models.CharField(max_length=10, choices=liste_choices.GENRE)
    promotion = models.CharField(
        max_length=10, choices=liste_choices.PROMO_CHOICES)
    date_naissance = models.DateField()
    numero_telephone = models.CharField(max_length=20)
    avatar = models.ImageField(
        upload_to='personne/avatar', default='personne/avatar/avatar.jpg')
    couverture = models.ImageField(
        upload_to='personne/couverture', default='personne/couverture/avatar.jpg')
    entreprise = models.CharField(max_length=100)
    technologie = models.ManyToManyField(Technologie)
    statut = models.CharField(
        max_length=50, choices=liste_choices.STATUT_CHOICES)
    filiere = models.CharField(
        max_length=50, choices=liste_choices.FILIERE_CHOICES)
    amis = models.ManyToManyField('self')

    def __str__(self):
        return self.user.last_name + " " + self.user.first_name


class Aine(Personne):
    person_type = 'aine'


class Projet(models.Model):
    titre_projet = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.titre_projet[:19] + "..."


class Stagiaire(Personne):
    person_type = 'stagiaire'
    projet = models.OneToOneField(
        Projet, on_delete=models.CASCADE, related_name="stagiaire")
    parrain = models.ManyToManyField(Aine, related_name="filieuls")


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

    def __str__(self):
        return self.nom


class Notification(models.Model):
    receveur = models.ManyToManyField(Personne, related_name='notifications')
    objet = models.CharField(max_length=50)
    contenu = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.objet


class Message(models.Model):
    auteur = models.ForeignKey(
        Personne, related_name="messages", on_delete=models.CASCADE)
    contenu = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.auteur.user.username

    def las_10_messages(self):
        return Message.objects.order_by('-date').all()[:10]
