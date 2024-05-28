from django import forms
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from gestion.models import MembreJury, EvaluationSoutenance

class EvaluationSoutenanceForm(forms.ModelForm):
    class Meta:
        model = EvaluationSoutenance
        fields = ['note', 'commentaires']

class UserUpdateForm(UserChangeForm):
    class Meta:
        model = MembreJury
        fields = ('nom', 'prenom', 'email')

class MembreJuryUpdateForm(forms.ModelForm):
    class Meta:
        model = MembreJury
        fields = ('nom', 'prenom', 'email', 'specialite')

class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = MembreJury
