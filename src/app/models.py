"""App models."""

from django.db import models


# Create your models here.
class Temp(models.Model):
    """Temp model."""

    temp = "temp model"

    def __str__(self: "Temp") -> str:
        """ToString Temp."""
        return f"{self.temp}"
