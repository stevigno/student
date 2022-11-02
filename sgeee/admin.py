from django.contrib import admin
from .models import Niveau, UniteEns
from django.contrib.auth.models import User
from enseignants.models import Professeur
from etudiants.models import Etudiant

class ProfesseurInline(admin.StackedInline):
    model = Professeur
    can_delete: False
    verbose_name_plural = 'professeur'

class EtudiantInline(admin.StackedInline):
    model = Etudiant
    can_delete: False
    verbose_name_plural = 'etudiant'

   


