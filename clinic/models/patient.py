from datetime import date

from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


dni_validator = RegexValidator(
    regex=r'^\d{8}$',
    message='DNI must contain exactly 8 digits.'
)


class Patient(models.Model):

    first_name = models.CharField(
        max_length=100
    )

    last_name = models.CharField(
        max_length=100
    )

    dni = models.CharField(
        max_length=8,
        unique=True,
        validators=[dni_validator]
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

    birth_date = models.DateField(
        null=True,
        blank=True
    )

    address = models.TextField(
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

        if self.birth_date:

            if self.birth_date > date.today():
                raise ValidationError(
                    "Birth date cannot be in the future."
                )

            age = (
                date.today().year
                - self.birth_date.year
            )

            if age > 120:
                raise ValidationError(
                    "Invalid age."
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