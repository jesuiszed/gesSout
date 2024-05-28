from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group, Permission
from .models import RoleUtilisateur, DirecteurThese, MembreJury, These, Soutenance, EvaluationSoutenance, Etudiant



# Define a new admin class for CustomUser
class RoleUtilisateurAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'role')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'first_name', 'last_name', 'role', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)

# Register your models here
admin.site.register(RoleUtilisateur, RoleUtilisateurAdmin)
admin.site.register(DirecteurThese)
admin.site.register(MembreJury)
admin.site.register(These)
admin.site.register(Soutenance)
admin.site.register(EvaluationSoutenance)
admin.site.register(Etudiant)
