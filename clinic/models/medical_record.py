from django.db import models

from .patient import Patient


class MedicalRecord(models.Model):

    patient = models.OneToOneField(
        Patient,
        on_delete=models.PROTECT
    )

    medical_history = models.TextField(
        null=True,
        blank=True
    )

    allergies = models.TextField(
        null=True,
        blank=True
    )

    general_observations = models.TextField(
        null=True,
        blank=True
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return str(self.patient)
