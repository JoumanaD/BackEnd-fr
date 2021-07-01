from typing import no_type_check
from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Etudiant(models.Model):
    IDetudiant = models.CharField(primary_key=True, max_length=8, validators=[MinLengthValidator(8)])
    nom = models.CharField(max_length=64)
    prenom = models.CharField(max_length=64)
    numTeleph = models.IntegerField()
    email = models.EmailField()
    SS_CHOICES = (
    ('Ayant Droit', 'Ayant Droit'),
    ('Etudiant', 'Etudiant'),
    ('Assuré Volontaire', 'Assuré Volontaire'),
    ('Etudiant Etranger', 'Etudiant Etranger'))
    TypeSS = models.CharField(max_length=64, choices = SS_CHOICES)
    CAM = models.CharField(max_length=64)
    inscrit = models.CharField(max_length=64)
    enseingnant = models.CharField(max_length=64)


    def __str__(self):
        return self.IDetudiant

class Fiche(models.Model):
    noFiche = models.AutoField(primary_key=True)
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE, related_name="etudiant")

    def __str__(self):
        return f"{self.noFiche} : {self.etudiant}"

class Adresse(models.Model):
    adresse_id = models.AutoField(primary_key=True)
    adr = models.CharField(max_length=64)
    codePostal = models.CharField(max_length=10)
    ville = models.CharField(max_length=64)
    pays = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.ville}, {self.pays}"

class Etablissement(models.Model):
    etab_id = models.AutoField(primary_key=True)
    raisonSociale = models.CharField(max_length=64)
    representationLegal = models.CharField(max_length=64)
    fonction = models.CharField(max_length=64)
    adresse = models.ForeignKey(Adresse, on_delete=models.CASCADE, related_name="adresse")
    noSiret = models.CharField(max_length=14, validators=[MinLengthValidator(14)], null=True)
    codeAPE = models.CharField(max_length=5, null=True)
    domaineDAct = models.CharField(max_length=64)
    effectif = models.IntegerField()

    def __str__(self):
        return f"{self.etab_id} : {self.raisonSociale} représenté par {self.representationLegal}"

class RHservice(models.Model):
    nom = models.CharField(max_length=64)
    prenom = models.CharField(max_length=64)
    numTeleph = models.IntegerField()
    email = models.EmailField()
    adresse_RH = models.ForeignKey(Adresse, on_delete=models.CASCADE, related_name="adresse_RH")
    etab_RH = models.ForeignKey(Etablissement, on_delete=models.CASCADE, related_name="etab_RH")

    def __str__(self):
        return f"RH : {self.nom}"

class Accueilservice(models.Model):
    adresse_Acc = models.ForeignKey(Adresse, on_delete=models.CASCADE, related_name="adresse_Acc")
    etab_Acc = models.ForeignKey(Etablissement, on_delete=models.CASCADE, related_name="etab_Acc")

    def __str__(self):
        return f"Service D'accueil : {self.adresse_Acc} pour Etablissement no : {self.etab_Acc}"