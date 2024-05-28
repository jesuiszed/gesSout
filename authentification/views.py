from django.contrib.auth import login as auth_login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('authentification:redirect_based_on_role')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
@login_required
def redirect_based_on_role(request):
    user = request.user
    if user.role == 'student':
        return redirect('etudiants:student_dashboard')
    elif user.role == 'thesis_director':
        return redirect('directeur:directeur_dashboard')
    elif user.role == 'jury_member':
        return redirect('jury:membre_jury_dashboard')
    else:
        return redirect('authentification:dashboard')

@login_required
def dashboard(request):
    return render(request, 'acceuil.html')

@login_required
def logout(request):
    return render(request, 'acceuil.html')


def custom_logout_view(request):
    logout(request)
    return redirect(reverse_lazy('authentification:login'))