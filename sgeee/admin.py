from django.contrib import admin
from .models import Niveau, UniteEns
from enseignants.models import Professeur
from etudiants.models import Etudiant

class NiveauAdmin(admin.ModelAdmin):
    list_display = ('nom_niveau', 'intitule')


class UniteEnsAdmin(admin.ModelAdmin):
    list_display = ('code', 'nom_unite')


admin.site.register(Niveau)    
admin.site.register(UniteEns)    


