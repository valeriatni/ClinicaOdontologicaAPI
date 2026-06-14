from django.db import models
from django.core.exceptions import ValidationError

from .budget import Budget
from .procedure import Procedure


class BudgetDetail(models.Model):

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
    ]

    budget = models.ForeignKey(
        Budget,
        on_delete=models.CASCADE
    )

    procedure = models.ForeignKey(
        Procedure,
        on_delete=models.PROTECT
    )

    quantity = models.PositiveIntegerField()

    unit_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    subtotal = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    item_status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    def clean(self):

        if self.quantity <= 0:
            raise ValidationError(
                "Quantity must be greater than zero."
            )

        if self.unit_price < 0:
            raise ValidationError(
                "Unit price cannot be negative."
            )

    def save(self, *args, **kwargs):

        self.subtotal = self.quantity * self.unit_price

        self.full_clean()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.procedure.name}"