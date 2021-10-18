"""Core app."""

# Django
from django.apps import AppConfig


class CoreAppConfig(AppConfig):
    """Core app config."""

    default_auto_field = "django.db.models.BigAutoField"
    name = 'bigbox.core'
    verbose_name = 'Cores'
