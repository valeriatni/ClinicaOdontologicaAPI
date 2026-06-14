from django.db import models
from django.core.exceptions import ValidationError

from .patient import Patient
from .suggested_treatment import SuggestedTreatment


class Budget(models.Model):

    STATUS_CHOICES = [
        ('Draft', 'Draft'),
        ('Sent', 'Sent'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
        ('Completed', 'Completed'),
    ]

    suggested_treatment = models.OneToOneField(
        SuggestedTreatment,
        on_delete=models.PROTECT
    )

    patient = models.ForeignKey(
        Patient,
        on_delete=models.PROTECT
    )

    issue_date = models.DateField()

    gross_total = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    discount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    net_total = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    budget_status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default='Draft'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def clean(self):

        if self.gross_total < 0:
            raise ValidationError(
                "Gross total cannot be negative."
            )

        if self.discount < 0:
            raise ValidationError(
                "Discount cannot be negative."
            )

        if self.discount > self.gross_total:
            raise ValidationError(
                "Discount cannot exceed gross total."
            )

        if self.net_total < 0:
            raise ValidationError(
                "Net total cannot be negative."
            )

    def save(self, *args, **kwargs):

        self.full_clean()

        super().save(*args, **kwargs)

    class Meta:

        ordering = ['-issue_date']

        indexes = [
            models.Index(fields=['patient'])
        ]

    def __str__(self):
        return f"Budget #{self.id}"