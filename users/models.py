from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Administrateur'),
        ('manager', 'Gestionnaire'),
        ('employee', 'Employé'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='admin')
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(unique=True)
    def __str__(self):
        return f"{self.get_full_name() or self.username} ({self.get_role_display()})"

    class Meta:
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"
