from rest_framework import routers
from django.urls import path, include
from . import views


router = routers.DefaultRouter()
router.register(r'vehicle-details', views.VehicleDetailsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
