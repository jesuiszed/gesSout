from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from .forms import TheseForm, UserUpdateForm, EtudiantUpdateForm, CustomPasswordChangeForm, CommentaireForm
from gestion.models import These

@login_required
def student_dashboard_view(request):
    user = request.user
    etudiant = getattr(user, 'etudiant', None)
    thesis = etudiant.these if etudiant else None

    thesis_form = TheseForm(instance=thesis)
    user_form = UserUpdateForm(instance=user)
    etudiant_form = EtudiantUpdateForm(instance=etudiant)
    password_form = CustomPasswordChangeForm(user=user)
    commentaire_form = CommentaireForm()

    if request.method == 'POST':
        if 'update_thesis' in request.POST:
            thesis_form = TheseForm(request.POST, instance=thesis)
            if thesis_form.is_valid():
                thesis_form.save()
                return redirect('etudiants:student_dashboard')
        elif 'update_account' in request.POST:
            user_form = UserUpdateForm(request.POST, instance=user)
            etudiant_form = EtudiantUpdateForm(request.POST, instance=etudiant)
            if user_form.is_valid() and etudiant_form.is_valid():
                user_form.save()
                etudiant_form.save()
                return redirect('etudiants:student_dashboard')
        elif 'change_password' in request.POST:
            password_form = CustomPasswordChangeForm(data=request.POST, user=user)
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)  # Important, pour mettre à jour la session avec le nouveau mot de passe
                return redirect('etudiants:student_dashboard')
        elif 'ajouter_commentaire' in request.POST:
            commentaire_form = CommentaireForm(request.POST)
            if commentaire_form.is_valid():
                commentaire = commentaire_form.save(commit=False)
                commentaire.etudiant = etudiant
                commentaire.save()
                thesis.commentaires.add(commentaire)
                thesis.save()

    return render(request, 'acceuil_etudiant.html', {
        'thesis_form': thesis_form,
        'user_form': user_form,
        'etudiant_form': etudiant_form,
        'password_form': password_form,
        'commentaire_form': commentaire_form,
        'thesis': thesis,
    })
