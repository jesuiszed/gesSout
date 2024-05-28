from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from .forms import EvaluationSoutenanceForm, CustomPasswordChangeForm, UserUpdateForm, MembreJuryUpdateForm
from gestion.models import MembreJury, Soutenance, EvaluationSoutenance

@login_required
def membre_jury_dashboard_view(request):
    user = request.user
    membre_jury = getattr(user, 'membrejury', None)
    soutenances = Soutenance.objects.filter(membres_jury=membre_jury)
    soutenances_evaluees = {}
    for soutenance in soutenances:
        evaluations = EvaluationSoutenance.objects.filter(soutenance=soutenance, membre_jury=membre_jury)
        soutenances_evaluees[soutenance.id] = evaluations

    evaluation_form = EvaluationSoutenanceForm()
    user_form = UserUpdateForm(instance=user)
    membre_jury_form = MembreJuryUpdateForm(instance=membre_jury)
    password_form = CustomPasswordChangeForm(user=user)

    if request.method == 'POST':
        if 'update_profile' in request.POST:
            user_form = UserUpdateForm(request.POST, instance=user)
            membre_jury_form = MembreJuryUpdateForm(request.POST, instance=membre_jury)
            if user_form.is_valid() and membre_jury_form.is_valid():
                user_form.save()
                membre_jury_form.save()
                return redirect('jury:membre_jury_dashboard')
        elif 'change_password' in request.POST:
            password_form = CustomPasswordChangeForm(data=request.POST, user=user)
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)
                return redirect('jury:membre_jury_dashboard')
        elif 'evaluation_soutenance' in request.POST:
            soutenance_id = request.POST.get('soutenance_id')
            soutenance = get_object_or_404(Soutenance, id=soutenance_id)
            evaluation_form = EvaluationSoutenanceForm(request.POST)
            if evaluation_form.is_valid():
                evaluation = evaluation_form.save(commit=False)
                evaluation.soutenance = soutenance
                evaluation.membre_jury = membre_jury
                evaluation.save()
                return redirect('jury:membre_jury_dashboard')
        elif 'update_evaluation' in request.POST:
            evaluation_id = request.POST.get('evaluation_id')
            evaluation = get_object_or_404(EvaluationSoutenance, id=evaluation_id)
            evaluation_form = EvaluationSoutenanceForm(request.POST, instance=evaluation)
            if evaluation_form.is_valid():
                evaluation_form.save()
                return redirect('jury:membre_jury_dashboard')
        elif 'delete_evaluation' in request.POST:
            evaluation_id = request.POST.get('evaluation_id')
            evaluation = get_object_or_404(EvaluationSoutenance, id=evaluation_id)
            evaluation.delete()
            return redirect('jury:membre_jury_dashboard')


    return render(request, 'acceuil_jury.html', {
        'soutenances': soutenances,
        'evaluation_form': evaluation_form,
        'user_form': user_form,
        'membre_jury_form': membre_jury_form,
        'password_form': password_form,
        'soutenances_evaluees': soutenances_evaluees,
    })
