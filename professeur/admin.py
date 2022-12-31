from django.contrib import admin
from .models import Professeur
# Register your models here.

class ProfesseurAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenoms', 'matricule', 'fonction', 'actifs', 'updated_at')
    list_filter = ('matricule', 'actifs')
    list_editable = ['nom', 'prenoms']

admin.site.register(Professeur, ProfesseurAdmin)