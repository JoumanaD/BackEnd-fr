# Generated by Django 3.2.4 on 2021-06-30 23:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20210701_0142'),
    ]

    operations = [
        migrations.CreateModel(
            name='RHservice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=64)),
                ('prenom', models.CharField(max_length=64)),
                ('numTeleph', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('adresse_RH', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adresse_RH', to='api.adresse')),
                ('etab_RH', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='etab_RH', to='api.etablissements')),
            ],
        ),
    ]
