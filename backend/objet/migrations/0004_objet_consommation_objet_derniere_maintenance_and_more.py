# Generated by Django 5.2 on 2025-04-12 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objet', '0003_alter_objet_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='objet',
            name='consommation',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='objet',
            name='derniere_maintenance',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='objet',
            name='localisation',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='objet',
            name='marque',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
