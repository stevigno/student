from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Etudiant(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length = 50)
    slug = models.CharField(max_length = 50)
    prenons = models.CharField(max_length = 100)
    matricule = models.CharField(max_length = 32, unique = True)
    actifs = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date= models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nom