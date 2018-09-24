from rest_framework import viewsets

from .models import Trip
from .serializers import TripsSerializer


class TripsViewSet(viewsets.ModelViewSet):
    """

    """
    queryset = Trip.objects.all()
    serializer_class = TripsSerializer

    def perform_create(self, serializer):
        serializer.save()
