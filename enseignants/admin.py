from django.contrib import admin
from .models import Professeur
# Register your models here.

class ProfesseurAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenoms', 'matricule', 'fonction', 'actifs', 'email', 'modified_date')
    prepopulated_fields = {'slug': ('nom')}

admin.site.register(Professeur)