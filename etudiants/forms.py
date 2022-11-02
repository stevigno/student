from django import forms
from .models import Etudiant


class StudentForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = ['nom', 'prenons', 'niveau', 'filiere', 'matricule', 'actifs']