from django.contrib import admin
from .models import Professeur
# Register your models here.

class ProfesseurAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenoms', 'matricule', 'fonction', 'actifs', 'adresse', 'updated_at')
    prepopulated_fields = {'slug_prof': ('nom',)}

admin.site.register(Professeur, ProfesseurAdmin)