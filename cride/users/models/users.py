"""User model."""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Utilities
from cride.utils.models import CRideModels


class User(CRideModels, AbstractUser):
    """User model.

    Extend form Django's Abstract User, change the username field
    to email and add some extra fields.

    """
    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={'unique': 'A user with that email already exists.'}
    )

    #RegexValidator is a class that validates a string using a regular expression.
    phone_regex = RegexValidator(
        #Can initialize with a signal plus or one numer, then 9 to 15 digits
        regex=r'\+?1?\d{9,15}$',#The regular expression that will be used to validate the input.
        message="Phone number must be entered in the format: +999999999. Up to 15 digits allowed"
    )

    # validators is a list of validators to run for this field
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    USERNAME_FIELD: str = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    is_client = models.BooleanField(
        'client',
        default=True,
        help_text=(
            'Help easily distinguish users and perform queries. '
            'Clients are the main type of user. '
        )
    )

    is_verified = models.BooleanField(
        'verified',
        default=False,
        help_text='Set to true when the user have verified its email address. '
    )

    def __str__(self) -> str:
        """Return username"""
        return self.username

    # get_full_name and get_short_name are required for the admin, is the format of the user in the admin
    def get_short_name(self) -> str:
        """Return username."""
        return self.username
