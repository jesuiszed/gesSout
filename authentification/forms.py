from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Nom d’utilisateur', max_length=254)
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)
