from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import *

app_name = 'directeur'

urlpatterns = [
    path('directeur_dashboard/', directeur_dashboard_view, name='directeur_dashboard'),

]
