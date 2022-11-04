from django.contrib import admin
from .models import UE, Question

# Register your models here.
class UEadmin(admin.ModelAdmin):
    list_display = ('student', 'tuteur','intitule', 'info', 'code')

class Questionadmin(admin.ModelAdmin):
    list_display = ('ue', 'question','reponse', 'critere')    

admin.site.register(UE, UEadmin)    
admin.site.register(Question, Questionadmin)    