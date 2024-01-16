# Generated by Django 4.2.9 on 2024-01-15 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentification', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('Créateur', 'Creator'), ('Abonné', 'Subscriber')], max_length=30, unique=True),
        ),
    ]
