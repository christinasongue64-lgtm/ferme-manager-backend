from django.db import models
from django.conf import settings


class Sale(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sales')
    animal = models.ForeignKey('animals.Animal', on_delete=models.SET_NULL, null=True, blank=True, related_name='sales')
    client_name = models.CharField(max_length=200, verbose_name="Nom du client")
    client_phone = models.CharField(max_length=30, blank=True, verbose_name="Téléphone client")
    date = models.DateField(verbose_name="Date de vente")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Quantité")
    unit_price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Prix unitaire (FCFA)")
    description = models.CharField(max_length=255, verbose_name="Description")
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def total_price(self):
        return self.quantity * self.unit_price

    def __str__(self):
        return f"Vente {self.id} — {self.client_name} — {self.date}"

    class Meta:
        verbose_name = "Vente"
        verbose_name_plural = "Ventes"
        ordering = ['-date']
