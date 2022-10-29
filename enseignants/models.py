from enum import unique
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Professeur(models.Model):
    nom = models.CharField(max_length = 50)
    prenom = models.CharField(max_length = 50)
    matricule = models.CharField(max_length =255, unique = True)
    grade = models.CharField(max_length = 100)
    fonction = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    date_enregistrment = models.DateTimeField()
    normal = models.ForeignKey(User, on_delete=models.CASCADE)