from rest_framework import serializers
from .models import Trip


class TripsSerializer(serializers.ModelSerializer):
    """

    """
    class Meta:
        model = Trip
        fields = ('from_country', 'to_country', 'from_city', 'to_city', 'departure_time')

    def create(self, validated_data):
        return Trip.objects.create(**validated_data)

