# Generated by Django 3.2.4 on 2021-07-02 11:21

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0009_auto_20210702_1321'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adresse',
            fields=[
                ('adresse_id', models.AutoField(primary_key=True, serialize=False)),
                ('adr', models.CharField(max_length=64)),
                ('codePostal', models.CharField(max_length=10)),
                ('ville', models.CharField(max_length=64)),
                ('pays', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Date',
            fields=[
                ('date_id', models.AutoField(primary_key=True, serialize=False)),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
                ('tempsPlein', models.BooleanField()),
                ('interuption', models.BooleanField()),
                ('date_interuption_debut', models.DateField(blank=True, null=True)),
                ('date_interuption_fin', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Etablissement',
            fields=[
                ('etab_id', models.AutoField(primary_key=True, serialize=False)),
                ('raisonSociale', models.CharField(max_length=64)),
                ('representationLegal', models.CharField(max_length=64)),
                ('fonction', models.CharField(max_length=64)),
                ('noSiret', models.CharField(blank=True, max_length=14, null=True, validators=[django.core.validators.MinLengthValidator(14)])),
                ('codeAPE', models.CharField(blank=True, max_length=5, null=True)),
                ('domaineDAct', models.CharField(max_length=64)),
                ('effectif', models.IntegerField()),
                ('adresse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adresse', to='api.adresse')),
            ],
        ),
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('IDetudiant', models.CharField(max_length=8, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(8)])),
                ('nom', models.CharField(max_length=64)),
                ('prenom', models.CharField(max_length=64)),
                ('numTeleph', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('TypeSS', models.CharField(choices=[('Ayant Droit', 'Ayant Droit'), ('Etudiant', 'Etudiant'), ('Assuré Volontaire', 'Assuré Volontaire'), ('Etudiant Etranger', 'Etudiant Etranger')], max_length=64)),
                ('CAM', models.CharField(max_length=64)),
                ('inscrit', models.CharField(max_length=64)),
                ('enseingnant', models.CharField(max_length=64)),
                ('adresse_etud', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='adresse_etud', to='api.adresse')),
            ],
        ),
        migrations.CreateModel(
            name='Gratification',
            fields=[
                ('gratif_id', models.AutoField(primary_key=True, serialize=False)),
                ('montant', models.IntegerField()),
                ('versement', models.CharField(choices=[('Chéque', 'Chéque'), ('Virement Bancaire', 'Virement Bancaire'), ('Espèce', 'Espèce')], max_length=30)),
                ('avantage', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tuteur',
            fields=[
                ('tuteur_id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=64)),
                ('prenom', models.CharField(max_length=64)),
                ('numTeleph', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('fonction', models.CharField(max_length=64)),
                ('service', models.CharField(max_length=64)),
                ('disponibilite', models.CharField(choices=[('Importante', 'Importante'), ('Partielle', 'Partielle'), ('Inexistante', 'Inexistante')], max_length=30)),
                ('adresse_Tuteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adresse_Tuteur', to='api.adresse')),
                ('etab', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='etab_Tuteur', to='api.etablissement')),
            ],
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('stage_id', models.AutoField(primary_key=True, serialize=False)),
                ('titre', models.CharField(max_length=64)),
                ('nbHeure', models.IntegerField()),
                ('gratification', models.BooleanField()),
                ('confidentialite', models.BooleanField()),
                ('description', models.TextField()),
                ('objectifs', models.TextField()),
                ('taches', models.TextField()),
                ('detail', models.TextField()),
                ('IDetudiant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stage_etudiant', to='api.etudiant')),
                ('date', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='date_stage', to='api.date')),
                ('gratification_detail', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gratification_stage', to='api.gratification')),
                ('tuteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tuteur_stage', to='api.tuteur')),
            ],
        ),
        migrations.CreateModel(
            name='RHservice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=64)),
                ('prenom', models.CharField(max_length=64)),
                ('numTeleph', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('adresse_RH', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adresse_RH', to='api.adresse')),
                ('etab_RH', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='etab_RH', to='api.etablissement')),
            ],
        ),
        migrations.CreateModel(
            name='Fiche',
            fields=[
                ('noFiche', models.AutoField(primary_key=True, serialize=False)),
                ('etudiant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='etudiant', to='api.etudiant')),
            ],
        ),
        migrations.CreateModel(
            name='Accueilservice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adresse_Acc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adresse_Acc', to='api.adresse')),
                ('etab_Acc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='etab_Acc', to='api.etablissement')),
            ],
        ),
    ]