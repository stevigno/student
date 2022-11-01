from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from etudiants.models import Etudiant


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class EtudiantForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = ["nom", "prenons", "matricule", "actifs", "niveau"]
