from enum import unique
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Professeur(models.Model):
    teacher = models.OneToOneField(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length = 50)
    slug = models.CharField(max_length = 50)
    prenoms = models.CharField(max_length = 70)
    matricule = models.CharField(max_length =255, unique = True)
    grade = models.CharField(max_length = 100)
    fonction = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    actifs = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom 
    