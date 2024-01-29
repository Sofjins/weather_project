from django.db import models


class CityInput(models.Model):
    """Model to create city instance."""
    name = models.CharField(max_length=50)
