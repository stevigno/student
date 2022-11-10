from django.contrib import admin
from .models import Etudiant
import admin_thumbnails


class EtudiantAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenons', 'actifs', 'filiere', 'adresse', 'updated_at')
    list_editable = ('actifs',)
    list_filter = ('genre','niveau')
    order_by = ('-genre','niveau')
    prepopulated_fields = {'slug': ('nom',)}


# Register your models here.
admin.site.register(Etudiant, EtudiantAdmin)