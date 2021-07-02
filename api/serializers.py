from rest_framework import serializers
from .models import Accueilservice, Adresse, Date, Etablissement, Etudiant, Fiche, Gratification, RHservice, Stage, Tuteur

class EtudiantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etudiant
        fields=('IDetudiant',
                'nom',
                'prenom',
                'numTeleph',
                'email',
                'adresse_etud',
                'TypeSS',
                'CAM',
                'inscrit',
                'enseingnant')

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

class DateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Date
        fields=('date_id',
                'date_debut',
                'date_fin',
                'tempsPlein',
                'interuption',
                'date_interuption_debut',
                'date_interuption_fin')

class GratificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gratification
        fields=('gratif_id',
                'montant',
                'versement',
                'avantage')

class StageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stage
        fields=('stage_id',
                'titre',
                'nbHeure',
                'gratification',
                'gratification_detail',
                'confidentialite',
                'date',
                'description',
                'objectifs',
                'taches',
                'detail',
                'IDetudiant',
                'tuteur')

class TuteurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tuteur
        fields=('tuteur_id',
                'nom',
                'prenom',
                'numTeleph',
                'email',
                'fonction',
                'service',
                'disponibilite',
                'adresse_Tuteur',
                'etab')