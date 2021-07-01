# Generated by Django 3.2.4 on 2021-07-01 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_rename_etablissements_etablissement'),
    ]

    operations = [
        migrations.CreateModel(
            name='Date',
            fields=[
                ('date_id', models.AutoField(primary_key=True, serialize=False)),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
                ('tempsPlein', models.BooleanField()),
                ('interuption', models.BooleanField()),
                ('date_interuption_debut', models.DateField(null=True)),
                ('date_interuption_fin', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gratification',
            fields=[
                ('gratif_id', models.AutoField(primary_key=True, serialize=False)),
                ('montant', models.IntegerField()),
                ('avantage', models.TextField()),
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
                ('dates', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='date_stage', to='api.date')),
                ('gratification_detail', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='gratification_stage', to='api.gratification')),
            ],
        ),
    ]
