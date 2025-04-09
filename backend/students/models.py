from django.db import models
from django.utils import timezone




class Student(models.Model):
    NIVEAU_CHOICES = [
        ('Débutant', 'Débutant'),
        ('intermédiaire', 'Intermédiaire'),
        ('avancé', 'Avancé'),
        ('expert', 'Expert'),
    ]

    name = models.CharField(max_length=140)
    course = models.CharField(max_length=140)
    grade = models.FloatField()
    email = models.EmailField(max_length=140, unique=True, default='example@example.com')
    pseudo = models.CharField(max_length=140, unique=True, null=True, blank=True)
    type_membre = models.CharField(max_length=100, null=True, blank=True)
    mot_de_passe = models.CharField(max_length=255, default='mdp')
    date_naissance = models.DateField(default=timezone.now)
    points = models.IntegerField(null=True, blank=True,default=0)
    total_connexions = models.IntegerField(null=True, blank=True, default=0)
    total_actions = models.IntegerField(null=True, blank=True, default=0)
    niveau_utilisateur = models.CharField(max_length=15, choices=NIVEAU_CHOICES, null=True, blank=True)
    date_inscription = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']


class ObjetConnecte(models.Model):
    TYPE_OBJET_CHOICES = [
        ('capteur', 'Capteur'),
        ('caméra', 'Caméra'),
        ('lampe', 'Lampe'),
        ('autre', 'Autre'),
    ]
    
    STATUT_CHOICES = [
        ('actif', 'Actif'),
        ('inactif', 'Inactif'),
    ]
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    type_objet = models.CharField(max_length=10, choices=TYPE_OBJET_CHOICES)
    statut = models.CharField(max_length=10, choices=STATUT_CHOICES, default='inactif')
    utilisateur = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=True)
    
    
    def __str__(self):
        return f"{self.nom} ({self.get_type_objet_display()}) - {self.get_statut_display()}"

    class Meta:
        ordering = ['name']