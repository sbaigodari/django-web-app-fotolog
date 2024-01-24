from django.contrib.auth.models import AbstractUser,Group
from django.db import models

class User(AbstractUser):

    class ROLE_CHOICES(models.TextChoices) :
  
        CREATOR = 'Créateur'
        SUBSCRIBER ='Abonné'

    CREATOR ='CREATOR',
    SUBSCRIBER= 'SUBSCRIBER'
    profile_photo = models.ImageField(verbose_name='Photo de profil')
    role = models.CharField(max_length=30,choices=ROLE_CHOICES.choices,verbose_name='Rôle')
    follows = models.ManyToManyField(
        'self',
        limit_choices_to={'role': CREATOR},
        symmetrical=False,
        verbose_name='suit',
    )

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)

        if self.role == self.CREATOR:
            
            group = Group.objects.get(name='creators')
            group.user_set.add(self)

        elif self.role == self.SUBSCRIBER:
            group = Group.objects.get(name='subscribers')
            group.user_set.add(self)


