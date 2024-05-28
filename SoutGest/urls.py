
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentification.urls')),
    path('etud/', include('etudiants.urls')),
    path('dir/', include('directeur.urls')),
    path('jury/', include('jury.urls')),

]
