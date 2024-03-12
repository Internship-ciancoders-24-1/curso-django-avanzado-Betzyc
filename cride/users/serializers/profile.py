"""Profile serializer."""

# Django REST Framework
from rest_framework import serializers

# Models
from cride.users.models import Profile


class ProfileModelSerializer(serializers.ModelSerializer):
    """Profile model serializer."""

    class Meta:
        """Meta class."""

        model = Profile
        fields = ( # These are the fields that are going to be serialized
            'picture',
            'biography',
            'rides_taken',
            'rides_offered',
            'reputation'
        )
        read_only_fields = (#   These are the fields that are going to be read only
            'rides_taken',
            'rides_offered',
            'reputation'
        )
