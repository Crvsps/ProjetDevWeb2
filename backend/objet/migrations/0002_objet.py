# Generated by Django 5.2 on 2025-04-10 07:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("objet", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Objet",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("slug", models.SlugField()),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("active", "Actif"),
                            ("inactive", "Inactif"),
                            ("maintenance", "Maintenance"),
                            ("out_of_service", "Hors-Service"),
                            ("busy", "Occupé"),
                        ],
                        default="inactive",
                        max_length=20,
                    ),
                ),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="upload/"),
                ),
                (
                    "thumbnail",
                    models.ImageField(blank=True, null=True, upload_to="upload/"),
                ),
                ("date_added", models.DateTimeField(auto_now_add=True)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="objets",
                        to="objet.category",
                    ),
                ),
            ],
            options={
                "ordering": ("-date_added",),
            },
        ),
    ]
