from django.db import models
from django.core.exceptions import ValidationError

from .budget import Budget
from .appointment import Appointment


class Payment(models.Model):

    METHOD_CHOICES = [
        ('Cash', 'Cash'),
        ('Card', 'Card'),
        ('Transfer', 'Transfer'),
        ('Insurance', 'Insurance'),
    ]

    budget = models.ForeignKey(
        Budget,
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )

    appointment = models.ForeignKey(
        Appointment,
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    payment_date = models.DateTimeField(
        auto_now_add=True
    )

    payment_method = models.CharField(
        max_length=20,
        choices=METHOD_CHOICES
    )

    reference_number = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def clean(self):

        if self.amount <= 0:
            raise ValidationError(
                "Payment amount must be greater than zero."
            )

        if not self.budget and not self.appointment:
            raise ValidationError(
                "Payment must be associated with a budget or an appointment."
            )

    def save(self, *args, **kwargs):

        self.full_clean()

        super().save(*args, **kwargs)

    class Meta:

        ordering = ['-payment_date']

        indexes = [
            models.Index(fields=['budget'])
        ]

    def __str__(self):
        return f"Payment #{self.id}"