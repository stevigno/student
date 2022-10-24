from django.db import models

# Create your models here.
class Etudiant(models.Model):
    nom = models.CharField(max_length = 32, null = False)
    prenom = models.CharField(max_length = 32, null = False)
    matricule = models.CharField(max_length = 32, null = False, unique = True)
    id_niveau = models.IntegerField(max_length = 10, null = False)
    login = models.CharField(max_length = 255, null = False)
    password = models.CharField(max_length = 255, null = False)
    date_enregistrment = models.DateTimeField()