# Generated by Django 5.2 on 2025-04-13 01:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objet', '0004_objet_consommation_objet_derniere_maintenance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objet',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='objets', to='objet.category'),
        ),
    ]
