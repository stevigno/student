from django.db import models

# Create your models here.
class Etudiant(models.Model):
    nom = models.CharField(max_length = 50)
    slug = models.SlugField(max_length = 50)
    prenons = models.CharField(max_length = 100)
    niveau = models.CharField(max_length = 50)
    filiere = models.CharField(max_length = 50)
    matricule = models.CharField(max_length = 32, unique = True)
    image = models.ImageField(upload_to='media/student/', default='media/images/default.png')
    adresse = models.CharField(max_length=200, blank = True)
    actifs = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nom