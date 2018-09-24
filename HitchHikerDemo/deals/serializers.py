from rest_framework import serializers

from .models import Deal


class DealSerializer(serializers.ModelSerializer):
    """

    """
    class Meta:
        model = Deal
        fields = ('id', 'shipment_id', 'trip_id', 'cost', 'is_traveler_confirmed','is_shipper_confirmed' )

    def perform_create(self, validation_data):
        return Deal.objects.create(**validation_data)
