from rest_framework import serializers

from .models import Shipment


class ShipmentSerializer(serializers.ModelSerializer):
    """

    """
    class Meta:
        model = Shipment
        fields = ('title', 'image', 'weight', 'height_dimesion','width_dimesion' ,'is_delivered')

    def perform_create(self, validation_data):
        return Shipment.objects.create(**validation_data)
