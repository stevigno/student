from django.shortcuts import render, redirect
from etudiants.models import Etudiant
from enseignants.models import Professeur

# Create your views here.
def home(request):
    student = Etudiant.objects.all()
    return render(request, 'home.html', {"student": student})
