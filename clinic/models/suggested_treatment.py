from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

from .medical_record import MedicalRecord
from .specialist import Specialist


class SuggestedTreatment(models.Model):

    STATUS_CHOICES = [
        ('Suggested', 'Suggested'),
        ('Budgeted', 'Budgeted'),
        ('In Progress', 'In Progress'),
        ('Finished', 'Finished'),
        ('Cancelled', 'Cancelled'),
    ]

    medical_record = models.ForeignKey(
        MedicalRecord,
        on_delete=models.PROTECT
    )

    specialist = models.ForeignKey(
        Specialist,
        on_delete=models.PROTECT
    )

    diagnosis = models.TextField()

    treatment_description = models.TextField()

    diagnosis_date = models.DateField()

    treatment_status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default='Suggested'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def clean(self):

        if self.diagnosis_date > timezone.now().date():
            raise ValidationError(
                "Diagnosis date cannot be in the future."
            )

        if not self.medical_record.is_active:
            raise ValidationError(
                "Medical record is inactive."
            )

        if not self.specialist.is_active:
            raise ValidationError(
                "Specialist is inactive."
            )

    def save(self, *args, **kwargs):

        self.full_clean()

        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-diagnosis_date']

        indexes = [
            models.Index(fields=['medical_record'])
        ]

    def __str__(self):
        return self.diagnosis