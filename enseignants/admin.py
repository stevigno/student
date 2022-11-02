from django.contrib import admin
from .models import Professeur
# Register your models here.

class ProfesseurAdmin(admin.ModelAdmin):
    list_display = ('nom_prof', 'prenoms', 'matricule', 'fonction', 'actifs', 'email', 'modified_date')
    prepopulated_fields = {'slug_prof': ('nom_prof',)}

admin.site.register(Professeur, ProfesseurAdmin)