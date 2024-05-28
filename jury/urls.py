from django.urls import path
from . import views

app_name = 'jury'

urlpatterns = [
    path('membre-jury/', views.membre_jury_dashboard_view, name='membre_jury_dashboard'),
    # Ajoutez d'autres URL au besoin
]
