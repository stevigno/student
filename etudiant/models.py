from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


User  = get_user_model()

NIVEAU = (
    ('niveau 1', 'niveau 1'),
    ('niveau 2', 'niveau 2'),
    ('niveau 3', 'niveau 3'),
    ('niveau 4', 'niveau 4'),
    ('niveau 5', 'niveau 5'),
    ('niveau 6', 'niveau 6'),
)

GENRE = (
    ('Homme', 'Homme'),
    ('Femme', 'Femme'),
)

class Etudiant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='etudiant', null=True)
    nom = models.CharField(max_length = 50)
    slug = models.SlugField(max_length = 50)
    prenons = models.CharField(max_length = 100)
    niveau = models.CharField(max_length = 50, choices=NIVEAU, default='niveau 1')
    genre = models.CharField(max_length = 50, choices=GENRE, default='Homme')
    filiere = models.CharField(max_length = 50)
    image = models.ImageField(upload_to='media/student/', default='media/images/default.png')
    adresse = models.CharField(max_length=200, blank = True)
    actifs = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Etudiants"
    
    def __str__(self):
        return '{} {} {}'.format(self.nom, self.prenons, self.genre)
    
    def get_absolute_url(self):
        return reverse("students_profile:student_profile_detail", args=[self.id])