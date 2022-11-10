from django import forms
from .models import Etudiant
from django.contrib.auth import get_user_model 





class EtudiantCreateForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        exclude = ('created_at', 'updated_at', 'user')

    def save(self, commit=True):
        user = super(EtudiantCreateForm, self).save(commit=False)
        if commit:
            user.student = True
            user.save()
        return user
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nom'].widget.attrs.update({'class':'form-control'})
        self.fields['prenom'].widget.attrs.update({'class':'form-control'})
        self.fields['niveau'].widget.attrs.update({'class':'form-control'})
        self.fields['genre'].widget.attrs.update({'class':'form-control'})
        self.fields['filiere'].widget.attrs.update({'class':'form-control'})
        self.fields['adresse'].widget.attrs.update({'class':'form-control'})
        self.fields['created_at'].widget.attrs.update({'class':'form-control'})



