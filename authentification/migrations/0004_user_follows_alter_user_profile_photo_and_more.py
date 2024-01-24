# Generated by Django 4.2.9 on 2024-01-24 10:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentification', '0003_auto_20210426_0359'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='follows',
            field=models.ManyToManyField(limit_choices_to={'role': ('CREATOR',)}, to=settings.AUTH_USER_MODEL, verbose_name='suit'),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_photo',
            field=models.ImageField(upload_to='', verbose_name='Photo de profil'),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('Créateur', 'Creator'), ('Abonné', 'Subscriber')], max_length=30, verbose_name='Rôle'),
        ),
    ]
