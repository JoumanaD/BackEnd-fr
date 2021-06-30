from rest_framework import serializers
from .models import Etudiant, Fiche

class EtudiantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etudiant
        fields=('IDetudiant',
                'nom',
                'prenom',
                'numTeleph',
                'email',
                'TypeSS',
                'inscrit')

class FicheSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fiche
        fields=('noFiche',
                'etudiant')