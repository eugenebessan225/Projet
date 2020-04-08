from django.contrib import admin
from pro_it.models import *

admin.site.register(Personne)
admin.site.register(Publication)
admin.site.register(Messages)


@admin.register(Stagiaire)
class AdminStagiaire(admin.ModelAdmin):
    list_display = ('nom','prenom','email','genre', 'filiere_cours', 'entreprise')

@admin.register(Aine)
class AdminAine(admin.ModelAdmin):
    list_display = ('nom','prenom','email', 'genre', 'niveau', 'filiere_faite', 'entreprise')

