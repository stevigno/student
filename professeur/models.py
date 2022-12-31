from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Professeur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length = 50)
    prenoms = models.CharField(max_length = 70)
    matricule = models.CharField(max_length =255, unique = True)
    image = models.ImageField(upload_to='media/professor/', default='media/professor/default.png')
    grade = models.CharField(max_length = 100)
    fonction = models.CharField(max_length = 100)
    adress = models.CharField(max_length = 100)
    actifs = models.BooleanField(default=True)
    date_admitted = models.DateTimeField(auto_now_add=False, help_text="Format: YYYY-MM-DD")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom

    def get_absolute_url(self):
        return reverse("teacher_profile:teacher_profile_detail", args = [self.pk])
