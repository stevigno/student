from statistics import mode
from django.db import models

# Create your models here.
class critere(models.Model):
    libelle = models.CharField(max_length = 255)

class niveau(models.Model):
    code = models.CharField(max_length = 32)
    intitule = models.CharField(max_length = 100)    

class question(models.Model):
    id_critere = models.IntegerField(null = False)
    intitule = models.CharField(max_length = 100)    