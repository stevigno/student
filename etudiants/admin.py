from django.contrib import admin
from .models import Etudiant

class EtudiantAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenons', 'matricule', 'actifs', 'niveau', 'filiere', 'modified_date')
    prepopulated_fields = {'slug': ('nom')}


# Register your models here.
admin.site.register(Etudiant)