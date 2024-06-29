from django.db import models


class VehicleDetails(models.Model):
    vin_number = models.CharField(max_length=30)
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    year = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.make} {self.model}"
