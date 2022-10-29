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


