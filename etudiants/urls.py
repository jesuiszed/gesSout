from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import *

app_name = 'etudiants'

urlpatterns = [
    path('student_dashboard/', student_dashboard_view, name='student_dashboard'),

]
