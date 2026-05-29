from django.db import models
from django.conf import settings


class HealthRecord(models.Model):
    TYPE_CHOICES = [
        ('vaccination', 'Vaccination'),
        ('treatment', 'Traitement'),
        ('checkup', 'Contrôle'),
        ('surgery', 'Chirurgie'),
        ('other', 'Autre'),
    ]

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='health_records')
    animal = models.ForeignKey('animals.Animal', on_delete=models.CASCADE, related_name='health_records')
    record_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    date = models.DateField(verbose_name="Date du soin")
    description = models.CharField(max_length=255, verbose_name="Description")
    medication = models.CharField(max_length=200, blank=True, verbose_name="Médicament")
    dose = models.CharField(max_length=100, blank=True, verbose_name="Dose")
    veterinarian = models.CharField(max_length=150, blank=True, verbose_name="Vétérinaire")
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Coût (FCFA)")
    next_date = models.DateField(null=True, blank=True, verbose_name="Prochain rappel")
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_record_type_display()} — {self.animal} — {self.date}"

    class Meta:
        verbose_name = "Suivi sanitaire"
        verbose_name_plural = "Suivis sanitaires"
        ordering = ['-date']
