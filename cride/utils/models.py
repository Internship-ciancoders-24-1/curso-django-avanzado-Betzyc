"""Django models utilities."""

# Django
from django.db import models


class CRideModels(models.Model):
    """Comparte Ride base model.

    CRideModel acts as an abstract base class from which every
    other model in the project will inherit. This class provides
    every table with the following attributes:
      + created (DateTime): Store the datetime the objects was created.
      + modified (DateTime): Store the datetime the objects was modified
    """

    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Date time on which the object was created'
    )

    modified = models.DateTimeField(
        'modified at',
        auto_now=True,
        help_text='Date time on which the object was last modified'
    )

    class Meta: # This class is used to define metadata for the model.
        """Meta options."""
        abstract = True # This option indicates that the model is an abstract class and is not in database.

        get_latest_by = 'created'# The field to use when ordering the queryset by the latest instance
        ordering = ['-created', '-modified'] # The default ordering for the objects of this model

""" class Student(CRideModels):
    Student model.
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()

    class Meta(CRideModels.Meta):
        db_table = 'students'
        verbose_name = 'student'
        verbose_name_plural = 'students'
        ordering = ['-first_name', '-last_name']

        proxy = True # This option indicates that the model is a proxy model. Proxy models are useful when you want to change the behavior of a model, without changing the model itself. The most common use for proxy models is to change the Python behavior of the model, without changing the database schema.
        """


