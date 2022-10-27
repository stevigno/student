from django.db import models

# Create your models here.
class Etudiant(models.Model):
    nom = models.CharField(max_length = 50)
    prenom = models.CharField(max_length = 32)
    matricule = models.CharField(max_length = 32, unique = True)
    id_niveau = models.IntegerField(max_length = 10)
    date_enregistrment = models.DateTimeField()