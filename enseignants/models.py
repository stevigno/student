from enum import unique
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Professeur(models.Model):
    login = models.CharField(max_length = 32, null = False)
    password = models.CharField(max_length = 255, null = False)
    nom = models.CharField(max_length = 32, null = False)
    prenom = models.CharField(max_length = 32, null = False)
    matricule = models.CharField(max_length = 32, null = False, unique = True)
    grade = models.CharField(max_length = 32, null = False)
    fonction = models.CharField(max_length = 32, null = False)
    email = models.CharField(max_length = 32, null = False)
    date_enregistrment = models.DateTimeField()