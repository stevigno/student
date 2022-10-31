from enum import auto
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Niveau(models.Model):
    nom_niveau = models.CharField(max_length = 200, unique=True) 
    intitule = models.CharField(max_length = 100)

class UniteEns(models.Model):
    code = models.CharField(max_length = 200, unique=True)
    nom_unite = models.CharField(max_length = 100)  
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE)  

class Filiere(models.Model):
    code_fil = models.CharField(max_length = 10, unique = True)
    nom_fil = models.CharField(max_length = 50)

class Session_evaluation(models.Model):
    code = models.CharField(max_length = 10, unique = True)
    date_session = models.DateField(auto_now_add=True)
    modified_date= models.DateField(auto_now=True)

class Question(models.Model):
    code_quest = models.CharField(max_length = 255)
    intitule = models.CharField(max_length = 50)
    critere = models.CharField(max_length = 50, unique = True)
    
class Filiere(models.Model):
    code_fil = models.CharField(max_length = 10, unique = True)
    nom_fil = models.CharField(max_length = 50)

class Filiere(models.Model):
    code_fil = models.CharField(max_length = 10, unique = True)
    nom_fil = models.CharField(max_length = 50)

class Filiere(models.Model):
    code_fil = models.CharField(max_length = 10, unique = True)
    nom_fil = models.CharField(max_length = 50)

class Filiere(models.Model):
    code_fil = models.CharField(max_length = 10, unique = True)
    nom_fil = models.CharField(max_length = 50)

