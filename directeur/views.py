from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from gestion.models import DirecteurThese, Soutenance
from .forms import DirecteurUpdateForm
from etudiants.forms import CustomPasswordChangeForm

@login_required
def directeur_dashboard_view(request):
    directeur = DirecteurThese.objects.get(utilisateur=request.user)
    soutenances = Soutenance.objects.filter(directeur_these=directeur)
    etudiants = directeur.etudiant_set.all()  # Récupérer les étudiants encadrés par ce directeur

    directeur_form = DirecteurUpdateForm(instance=directeur)
    password_form = CustomPasswordChangeForm(user=request.user)

    if request.method == 'POST':
        if 'update_account' in request.POST:
            directeur_form = DirecteurUpdateForm(request.POST, instance=directeur)
            if directeur_form.is_valid():
                directeur_form.save()
                return redirect('d:directeur_dashboard')
        elif 'change_password' in request.POST:
            password_form = CustomPasswordChangeForm(data=request.POST, user=request.user)
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)  # Important, pour mettre à jour la session avec le nouveau mot de passe
                return redirect('')

    return render(request, 'acceuil_directeur.html', {
        'directeur_form': directeur_form,
        'password_form': password_form,
        'soutenances': soutenances,
        'etudiants': etudiants,  # Passer les étudiants encadrés au modèle HTML
    })
