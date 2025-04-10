# Generated by Django 5.1.7 on 2025-04-09 21:45

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("students", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="date_inscription",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="student",
            name="date_naissance",
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="student",
            name="email",
            field=models.EmailField(
                default="example@example.com", max_length=140, unique=True
            ),
        ),
        migrations.AddField(
            model_name="student",
            name="mot_de_passe",
            field=models.CharField(default="mdp", max_length=255),
        ),
        migrations.AddField(
            model_name="student",
            name="niveau_utilisateur",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Débutant", "Débutant"),
                    ("intermédiaire", "Intermédiaire"),
                    ("avancé", "Avancé"),
                    ("expert", "Expert"),
                ],
                max_length=15,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="student",
            name="points",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name="student",
            name="pseudo",
            field=models.CharField(blank=True, max_length=140, null=True, unique=True),
        ),
        migrations.AddField(
            model_name="student",
            name="total_actions",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name="student",
            name="total_connexions",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name="student",
            name="type_membre",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.CreateModel(
            name="ObjetConnecte",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "type_objet",
                    models.CharField(
                        choices=[
                            ("capteur", "Capteur"),
                            ("caméra", "Caméra"),
                            ("lampe", "Lampe"),
                            ("autre", "Autre"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "statut",
                    models.CharField(
                        choices=[("actif", "Actif"), ("inactif", "Inactif")],
                        default="inactif",
                        max_length=10,
                    ),
                ),
                (
                    "utilisateur",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="students.student",
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
            },
        ),
    ]
