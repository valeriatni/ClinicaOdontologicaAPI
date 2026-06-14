from datetime import datetime

from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

from .patient import Patient
from .specialist import Specialist


class Appointment(models.Model):

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Waiting', 'Waiting'),
        ('In Consultation', 'In Consultation'),
        ('Attended', 'Attended'),
        ('Cancelled', 'Cancelled'),
        ('No Show', 'No Show'),
    ]

    patient = models.ForeignKey(
        Patient,
        on_delete=models.PROTECT
    )

    specialist = models.ForeignKey(
        Specialist,
        on_delete=models.PROTECT
    )

    appointment_date = models.DateField()

    appointment_time = models.TimeField()

    reason = models.TextField()

    appointment_status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def clean(self):

        appointment_datetime = datetime.combine(
            self.appointment_date,
            self.appointment_time
        )

        if appointment_datetime < timezone.now().replace(tzinfo=None):
            raise ValidationError(
                "Appointment cannot be scheduled in the past."
            )

        if self.appointment_time.hour < 8:
            raise ValidationError(
                "Clinic opens at 08:00."
            )

        if self.appointment_time.hour >= 18:
            raise ValidationError(
                "Clinic closes at 18:00."
            )

    def save(self, *args, **kwargs):

        self.full_clean()

        super().save(*args, **kwargs)

    class Meta:

        unique_together = (
            'specialist',
            'appointment_date',
            'appointment_time'
        )

        ordering = ['appointment_date']

    def __str__(self):
        return f"{self.patient} - {self.appointment_date}"