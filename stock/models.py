from django.db import models
from django.conf import settings


class StockItem(models.Model):
    CATEGORY_CHOICES = [
        ('aliment', 'Aliment'),
        ('medicament', 'Médicament'),
        ('equipement', 'Équipement'),
        ('autre', 'Autre'),
    ]

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='stock_items')
    name = models.CharField(max_length=200, verbose_name="Nom du produit")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Quantité")
    unit = models.CharField(max_length=50, verbose_name="Unité (kg, L, pièces…)")
    min_quantity = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Seuil d'alerte")
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Prix unitaire (FCFA)")
    supplier = models.CharField(max_length=200, blank=True, verbose_name="Fournisseur")
    expiry_date = models.DateField(null=True, blank=True, verbose_name="Date d'expiration")
    notes = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def is_low(self):
        return self.quantity <= self.min_quantity

    @property
    def total_value(self):
        return self.quantity * self.unit_price

    def __str__(self):
        return f"{self.name} ({self.category}) — {self.quantity} {self.unit}"

    class Meta:
        verbose_name = "Stock"
        verbose_name_plural = "Stocks"
        ordering = ['category', 'name']


class StockMovement(models.Model):
    MOVEMENT_CHOICES = [
        ('in', 'Entrée'),
        ('out', 'Sortie'),
    ]

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='stock_movements')
    item = models.ForeignKey(StockItem, on_delete=models.CASCADE, related_name='movements')
    movement_type = models.CharField(max_length=5, choices=MOVEMENT_CHOICES)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    reason = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_movement_type_display()} {self.quantity} — {self.item.name}"

    class Meta:
        verbose_name = "Mouvement de stock"
        verbose_name_plural = "Mouvements de stock"
        ordering = ['-date']
