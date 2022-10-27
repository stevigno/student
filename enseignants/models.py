from enum import unique
from django.db import models

# Create your models here.
class Professeur(models.Model):
    nom = models.CharField(max_length = 50)
    prenom = models.CharField(max_length = 50)
    matricule = models.CharField(max_length =255, unique = True)
    grade = models.CharField(max_length = 100)
    fonction = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    date_enregistrment = models.DateTimeField()