from django.db import models
from sgeee.models import Niveau
from django.contrib.auth.models import User

# Create your models here.
class Etudiant(models.Model):
    nom = models.CharField(max_length = 100)
    slug = models.CharField(max_length = 100)
    prenons = models.CharField(max_length = 100)
    matricule = models.CharField(max_length = 32, unique = True)
    actifs = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date= models.DateTimeField(auto_now=True)
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE)
    normal = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        
        return self.nom