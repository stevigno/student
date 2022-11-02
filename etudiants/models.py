from django.db import models

# Create your models here.
class Etudiant(models.Model):
    nom = models.CharField(max_length = 50)
    slug = models.CharField(max_length = 50)
    prenons = models.CharField(max_length = 100)
    niveau = models.CharField(max_length = 50)
    filiere = models.CharField(max_length = 50)
    matricule = models.CharField(max_length = 32, unique = True)
    actifs = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date= models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nom, self.niveau, self.matricule