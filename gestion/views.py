# views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import RoleUtilisateur

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')  # Redirection vers la page de profil
        else:
            # Gérer les cas d'authentification invalide
            return render(request, 'login.html', {'error': True})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirection vers la page de connexion

@login_required
def profile_view(request):
    user = request.user
    if user.role == 'student':
        # Gérer le cas de l'étudiant
        return render(request, 'student_profile.html', {'user': user})
    elif user.role == 'thesis_director':
        # Gérer le cas du directeur de thèse
        return render(request, 'director_profile.html', {'user': user})
    elif user.role == 'jury_member':
        # Gérer le cas du membre du jury
        return render(request, 'jury_profile.html', {'user': user})
    else:
        # Gérer les autres rôles
        return render(request, 'profile.html', {'user': user})

@login_required
def home_view(request):
    return render(request, 'home.html')
