from django.contrib import admin
from .models import Etudiant

class EtudiantAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenons', 'matricule', 'actifs', 'niveau', 'modified_date')
    prepopulated_fields = {'slug': ('name')}


# Register your models here.
admin.site.register(Etudiant)