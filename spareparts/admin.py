from django.contrib import admin
from .models import VehicleDetails


class VehicleDetailsAdmin(admin.ModelAdmin):
    list_display = ['make', 'model', 'year', 'vin_number']


admin.site.register(VehicleDetails, VehicleDetailsAdmin)
