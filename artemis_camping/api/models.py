from django.db import models

# Create your models here.

# Pending
class Message(models.Model):
    pass


    """Uses coordinates for working with Google Places API and Open Weather API"""
    """Dates data needs to be adjusted to work with Open Weather API """
class Trip(models.Model):
    name = models.CharField("Trip Name", max_length=50)
    start_latitude = models.DecimalField(
        max_digits=11, decimal_places=7, null=False, blank=True
    )
    start_longitude = models.DecimalField(
        max_digits=11, decimal_places=7, null=False, blank=True
    )
    destination_latitude = models.DecimalField(
        max_digits=11, decimal_places=7, null=False, blank=True
    )
    destination_longitude = models.DecimalField(
        max_digits=11, decimal_places=7, null=False, blank=True
    )
    start_date = models.DateField()
    end_date = models.DateField()
    difficulty = models.IntegerChoices("Difficulty", "Easy Medium Hard")
