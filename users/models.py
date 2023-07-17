from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from .managers import UserManager


class User(AbstractUser):
    """
    Custom User model representing a user in the system.

    Inherits from Django's AbstractUser class and adds additional fields for user details.
    """

    home_address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True,
        validators=[MinValueValidator(-90), MaxValueValidator(90)],
    )
    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True,
        validators=[MinValueValidator(-180), MaxValueValidator(180)],
    )

    objects = UserManager()

    def __str__(self):
        return self.username
