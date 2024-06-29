from django.db import models


class Vehicle(models.Model):
    vin_number = models.CharField(max_length=20, primary_key=True)
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    year = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.make} {self.model}"
