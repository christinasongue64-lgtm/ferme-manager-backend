from django.db import models
from django.conf import settings


class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('alimentation', 'Alimentation'),
        ('veterinaire', 'Vétérinaire'),
        ('equipement', 'Équipement'),
        ('salaire', 'Salaire'),
        ('transport', 'Transport'),
        ('autre', 'Autre'),
    ]

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='expenses')
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Montant (FCFA)")
    date = models.DateField(verbose_name="Date")
    supplier = models.CharField(max_length=200, blank=True, verbose_name="Fournisseur / Payé à")
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_category_display()} — {self.description} — {self.amount} FCFA"

    class Meta:
        verbose_name = "Dépense"
        verbose_name_plural = "Dépenses"
        ordering = ['-date']
