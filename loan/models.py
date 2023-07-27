from django.db import models
from loan.constants import GENDER_CHOICES
from utils.validators import dni_validator


class Loan(models.Model):
    dni = models.CharField(
        max_length=8,
        validators=[dni_validator],
        null=False,
        blank=False,
        db_index=True,
        unique=True,
    )
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, null=False, blank=False
    )

    email = models.EmailField(null=False, blank=False)
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, blank=False
    )

    def __str__(self):
        return f"{self.dni}-{self.first_name} {self.last_name}"
