from rest_framework import viewsets

from .models import Trip
from .serializers import TripsSerializer


class TripsViewSet(viewsets.ModelViewSet):
    """

    """
    _trips = Trip.objects.all()
    serializer_class = TripsSerializer



