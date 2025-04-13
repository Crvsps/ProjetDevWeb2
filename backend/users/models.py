from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class UserProfile(models.Model):
    GENDER_CHOICES = (('Homme', 'Homme'),
        ('Femme', 'Femme'),
        ('Autre', 'Autre'),)
    
    USER_TYPE_CHOICES =(
        ('Élève', 'Élève'),
        ('Professeur', 'Professeur'),
        ('Parent', 'Parent'),
        ('Administration', 'Administration'),
        ('Maintenance','Maintenance')
    )
        
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, null=True, blank=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='Élève')
    photo = models.ImageField(upload_to='upload/', null=True, blank=True)
    points = models.IntegerField(default=0)
    
    def __str__(self):
        return self.user.username
        

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)