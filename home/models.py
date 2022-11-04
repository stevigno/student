from django.db import models
from professeur.models import Professeur
from etudiant.models import Etudiant

# Create your models here.
class UE(models.Model):
    code = models.CharField(max_length = 150)
    intitule = models.CharField(max_length = 150)
    info = models.CharField(max_length = 150)
    tuteur = models.ForeignKey(Professeur, on_delete=models.CASCADE)
    student = models.ForeignKey(Etudiant, on_delete=models.CASCADE)

reponse = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),

    )

class Question(models.Model):
    question = models.CharField(max_length = 255)
    reponse = models.CharField(max_length = 255, choices = reponse)
    critere = models.CharField(max_length = 255)
    ue = models.ForeignKey(UE, on_delete=models.CASCADE)
