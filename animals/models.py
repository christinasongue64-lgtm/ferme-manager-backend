from django.db import models
from django.conf import settings
import uuid


class Animal(models.Model):
    TYPE_CHOICES = [
        ('volaille', 'Volaille'),
        ('porc', 'Porc'),
        ('bovin', 'Bovin'),
        ('ovin', 'Ovin'),
        ('caprin', 'Caprin'),
        ('autre', 'Autre'),
    ]
    SEX_CHOICES = [
        ('male', 'Mâle'),
        ('femelle', 'Femelle'),
    ]
    STATUS_CHOICES = [
        ('Vivant', 'Vivant'),
        ('Vendu', 'Vendu'),
        ('Décédé', 'Décédé'),
        ('Transféré', 'Transféré'),
    ]
    ENTRY_CHOICES = [
        ('achat', 'Achat'),
        ('naissance', 'Naissance'),
        ('don', 'Don'),
    ]

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='animals')
    identifier = models.CharField(max_length=50, unique=True, blank=True)
    name = models.CharField(max_length=100, blank=True)
    animal_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    breed = models.CharField(max_length=100, blank=True, verbose_name="Race")
    sex = models.CharField(max_length=10, choices=SEX_CHOICES, default='inconnu')
    birth_date = models.DateField(null=True, blank=True, verbose_name="Date de naissance")
    entry_date = models.DateField(verbose_name="Date d'entrée")
    entry_type = models.CharField(max_length=20, choices=ENTRY_CHOICES, default='achat')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Vivant')
    weight = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, verbose_name="Poids (kg)")
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.identifier:
            prefix = self.animal_type[:3].upper()
            self.identifier = f"{prefix}-{uuid.uuid4().hex[:6].upper()}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.identifier} — {self.get_animal_type_display()} ({self.name or 'Sans nom'})"

    class Meta:
        verbose_name = "Animal"
        verbose_name_plural = "Animaux"
        ordering = ['-entry_date']
