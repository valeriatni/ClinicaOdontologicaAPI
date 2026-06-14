from django.db import models
from django.core.exceptions import ValidationError

from .specialty import Specialty


class Specialist(models.Model):

    specialty = models.ForeignKey(
        Specialty,
        on_delete=models.PROTECT
    )

    first_name = models.CharField(
        max_length=100
    )

    last_name = models.CharField(
        max_length=100
    )

    license_number = models.CharField(
        max_length=50,
        unique=True
    )

    phone = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )

    email = models.EmailField(
        unique=True,
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

    def clean(self):

        if len(self.license_number) < 5:
            raise ValidationError(
                "License number is too short."
            )

        if not self.specialty.is_active:
            raise ValidationError(
                "Selected specialty is inactive."
            )

    def save(self, *args, **kwargs):

        self.first_name = self.first_name.upper()
        self.last_name = self.last_name.upper()

        self.full_clean()

        super().save(*args, **kwargs)

    class Meta:
        ordering = ['last_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"