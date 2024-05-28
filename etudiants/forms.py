from django import forms
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from gestion.models import These, RoleUtilisateur, Etudiant, Commentaire


class TheseForm(forms.ModelForm):
    class Meta:
        model = These
        fields = ['titre', 'resume',  'rapport']
        widgets = {
            'date_soutenance': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['texte']
        widgets = {
            'texte': forms.Textarea(attrs={'rows': 3}),  # Ajustez la taille de la zone de texte selon vos préférences
        }
class UserUpdateForm(UserChangeForm):
    class Meta:
        model = RoleUtilisateur
        fields = ['first_name', 'last_name', 'email']

class EtudiantUpdateForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = ['nom', 'prenom', 'email']

class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = RoleUtilisateur
        fields = ['old_password', 'new_password1', 'new_password2']


