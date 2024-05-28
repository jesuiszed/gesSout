from django.urls import path
from .views import login_view, dashboard, redirect_based_on_role, custom_logout_view

app_name = 'authentification'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', custom_logout_view, name='logout'),
    path('redirect/', redirect_based_on_role, name='redirect_based_on_role'),
    path('dashboard/', dashboard, name='dashboard'),
]
