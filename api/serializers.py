from rest_framework import serializers
from .models import Accueilservice, Adresse, Etablissement, Etudiant, Fiche, RHservice

class EtudiantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etudiant
        fields=('IDetudiant',
                'nom',
                'prenom',
                'numTeleph',
                'email',
                'TypeSS',
                'CAM',
                'inscrit')

class FicheSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fiche
        fields=('noFiche',
                'etudiant')

class AdresseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adresse
        fields=('adresse_id',
                'adr',
                'codePostal',
                'ville',
                'pays')

class EtablissementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etablissement
        fields=('etab_id',
                'raisonSociale',
                'representationLegal',
                'fonction',
                'adresse',
                'noSiret',
                'codeAPE',
                'domaineDAct',
                'effectif')


class RHserviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = RHservice
        fields=('nom',
                'prenom',
                'numTeleph',
                'email',
                'adresse_RH',
                'etab_RH')

class AccueilserviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accueilservice
        fields=('adresse_Acc',
                'etab_Acc')