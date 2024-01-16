from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):

    class ROLE_CHOICES(models.TextChoices) :
  
        CREATOR = 'Créateur'
        SUBSCRIBER ='Abonné'

    CREATOR ='CREATOR',
    SUBSCRIBER= 'SUBSCRIBER'
    profile_photo = models.ImageField(verbose_name='Photo de profil')
    role = models.CharField(max_length=30,choices=ROLE_CHOICES.choices,verbose_name='Rôle')
