# Generated by Django 3.2.4 on 2021-06-30 22:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_etudiant_typess'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etudiant',
            name='IDetudiant',
            field=models.CharField(max_length=4, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(4)]),
        ),
    ]
