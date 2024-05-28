from django import forms
from django.contrib.auth.forms import UserChangeForm
from gestion.models import DirecteurThese

class DirecteurUpdateForm(UserChangeForm):
    class Meta:
        model = DirecteurThese
        fields = ('nom', 'prenom', 'email')  # Champs à afficher pour la mise à jour des informations personnelles du directeur
