from django.contrib import admin
from .models import Date, Etudiant, Fiche, Adresse, Etablissement, Gratification, RHservice, Accueilservice, Stage, Tuteur

# Register your models here.
admin.site.register(Etudiant)
admin.site.register(Fiche)
admin.site.register(Adresse)
admin.site.register(Etablissement)
admin.site.register(RHservice)
admin.site.register(Accueilservice)
admin.site.register(Date)
admin.site.register(Gratification)
admin.site.register(Stage)
admin.site.register(Tuteur)
