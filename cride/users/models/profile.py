"""Profile model."""

# Django
from django.db import models

# Utilities
from cride.utils.models import CRideModels


class Profile(CRideModels):
    """Profile model.

    A profile holds a user's public data like biography, picture, and
    statistics.
    """

    user = models.OneToOneField('users.User', on_delete=models.CASCADE)

    picture = models.ImageField(
        'profile picture',
        upload_to='users/pictures/',
        blank=True,
        null=True
    )

    biography = models.TextField(max_length=501, blank=True)

    # Stats
    rides_taken = models.PositiveIntegerField(default=0)#The number of rides a user has taken
    rides_offered = models.PositiveBigIntegerField(default=0)#The number of rides a user has offered
    reputation = models.FloatField(#The reputation of the user
        default=5.0,
        help_text="User's reputation based on the rides taken and offered."
    )

    def __str__(self):
        """Return user's str representation."""
        return str(self.user)
