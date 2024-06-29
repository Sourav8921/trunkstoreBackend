from django.shortcuts import render
from rest_framework import viewsets
from .models import VehicleDetails
from .serializers import VehicleDetailsSerializer


class VehicleDetailsViewSet(viewsets.ModelViewSet):
    queryset = VehicleDetails.objects.all()
    serializer_class = VehicleDetailsSerializer


