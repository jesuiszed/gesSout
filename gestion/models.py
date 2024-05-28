from django.contrib.auth.models import AbstractUser
from django.db import models

class RoleUtilisateur(AbstractUser):
    # Ajoutez des champs supplémentaires ici
    role_choices = [
        ('student', 'Étudiant'),
        ('thesis_director', 'Directeur de thèse'),
        ('jury_member', 'Membre du jury'),
    ]
    role = models.CharField(max_length=20, choices=role_choices)
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name='customuser_set',
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='customuser_set',
        related_query_name='user',
    )

class DirecteurThese(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField()
    utilisateur = models.OneToOneField(RoleUtilisateur, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class MembreJury(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField()
    specialite = models.CharField(max_length=100)
    utilisateur = models.OneToOneField(RoleUtilisateur, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class Soutenance(models.Model):
    titre_these = models.CharField(max_length=200)
    date_heure = models.DateTimeField()
    lieu = models.CharField(max_length=200)
    directeur_these = models.ForeignKey(DirecteurThese, on_delete=models.CASCADE)
    membres_jury = models.ManyToManyField(MembreJury)

    def __str__(self):
        return self.titre_these

class EvaluationSoutenance(models.Model):
    soutenance = models.ForeignKey(Soutenance, on_delete=models.CASCADE)
    membre_jury = models.ForeignKey(MembreJury, on_delete=models.CASCADE)
    note = models.FloatField()
    commentaires = models.TextField()

    def __str__(self):
        return f"{self.soutenance} - {self.membre_jury}"

class Etudiant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField()
    these = models.OneToOneField('These', on_delete=models.CASCADE, null=True, blank=True, related_name='etudiant_these')
    directeur_these = models.ForeignKey(DirecteurThese, on_delete=models.CASCADE, null=True, blank=True)
    utilisateur = models.OneToOneField(RoleUtilisateur, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nom


class These(models.Model):
    titre = models.CharField(max_length=200)
    resume = models.TextField()
    directeur_these = models.ForeignKey(DirecteurThese, on_delete=models.CASCADE)
    date_soutenance = models.DateTimeField()
    membres_jury = models.ManyToManyField(MembreJury, null=True, blank=True)
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE, null=True, blank=True, related_name='theses')
    rapport = models.FileField(upload_to='rapport', null=True, blank=True)
    commentaires = models.TextField( null=True, blank=True)

    def __str__(self):
        return self.titre


class Commentaire(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE, related_name='commentaires')
    texte = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commentaire de {self.etudiant.nom} le {self.date_creation}"
