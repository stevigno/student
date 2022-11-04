from django.db import models

# Create your models here.
class Professeur(models.Model):
    nom = models.CharField(max_length = 50)
    slug_prof = models.SlugField(max_length = 50)
    prenoms = models.CharField(max_length = 70)
    matricule = models.CharField(max_length =255, unique = True)
    grade = models.CharField(max_length = 100)
    fonction = models.CharField(max_length = 100)
    adresse = models.CharField(max_length = 100)
    actifs = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom
