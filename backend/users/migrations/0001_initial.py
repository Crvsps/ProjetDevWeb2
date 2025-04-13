# Generated by Django 5.2 on 2025-04-13 13:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Homme', 'Homme'), ('Femme', 'Femme'), ('Autre', 'Autre')], max_length=20, null=True)),
                ('user_type', models.CharField(choices=[('Élève', 'Élève'), ('Professeur', 'Professeur'), ('Parent', 'Parent'), ('Administration', 'Administration'), ('Maintenance', 'Maintenance')], default='Élève', max_length=20)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='upload/')),
                ('points', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
