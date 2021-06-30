from django.db import models

# Create your models here.
class Etudiant(models.Model):
    IDetudiant = models.CharField(primary_key=True, max_length=8)
    nom = models.CharField(max_length=64)
    prenom = models.CharField(max_length=64)
    numTeleph = models.IntegerField()
    email = models.EmailField()
    SS_CHOICES = (
    ('1', 'Ayant Droit'),
    ('2', 'Etudiant'),
    ('3', 'Assuré Volontaire'),
    ('4', 'Etudiant Etranger'))
    TypeSS = models.CharField(max_length=64, choices = SS_CHOICES)
    inscrit = models.CharField(max_length=64)

    def __str__(self):
        return self.IDetudiant

class Fiche(models.Model):
    noFiche = models.AutoField(primary_key=True)
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE, related_name="etudiant")

    def __str__(self):
        return f"{self.noFiche} : {self.etudiant}"
