from enum import unique
from django.db import models

# Create your models here.
class Professeur(models.Model):
    nom = models.CharField(max_length = 50)
    slug = models.CharField(max_length = 50)
    prenoms = models.CharField(max_length = 70)
    matricule = models.CharField(max_length =255, unique = True)
    grade = models.CharField(max_length = 100)
    fonction = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = 'photos/products')
    actifs = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom, self.matricule
    