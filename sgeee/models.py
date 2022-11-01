from enum import auto
from django.db import models
from django.contrib.auth.models import User

from etudiants.models import Etudiant
from enseignants.models import Professeur

# Create your models here.

class UniteEns(models.Model):
    etudiant = models.CharField(max_length = 200, unique=True)
    nom_unite = models.CharField(max_length = 100)  
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)  
    Professeur = models.ForeignKey(Professeur, on_delete=models.CASCADE)  


class Session_evaluation(models.Model):
    code = models.CharField(max_length = 10, unique = True)
    nom_ses = models.CharField(max_length = 50)
    date_session = models.DateField(auto_now_add=True)
    modified_date= models.DateField(auto_now=True)

class Question(models.Model):
    code_quest = models.CharField(max_length = 255)
    intitule = models.CharField(max_length = 50)
    critere = models.CharField(max_length = 50, unique = True)

class Reponse(models.Model):
    etudiant = models.ManyToManyField(Etudiant)
    professeur = models.ForeignKey(Professeur, on_delete=models.CASCADE)
    intitule = models.TextField(max_length = 50)
    code_rep = models.CharField(max_length = 50, unique = True)
    

