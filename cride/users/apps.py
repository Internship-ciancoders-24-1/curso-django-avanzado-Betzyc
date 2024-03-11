"""Users app."""

# Django
from django.apps import AppConfig


class UsersAppConfig(AppConfig):
    """Users app config."""

    name = 'cride.users' # This is the application name, for the package name. cride/users
    verbose_name: str = 'Users'
