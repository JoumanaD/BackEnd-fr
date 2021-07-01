from django.contrib import admin
from .models import Etudiant, Fiche, Adresse, Etablissement, RHservice, Accueilservice

# Register your models here.
admin.site.register(Etudiant)
admin.site.register(Fiche)
admin.site.register(Adresse)
admin.site.register(Etablissement)
admin.site.register(RHservice)
admin.site.register(Accueilservice)