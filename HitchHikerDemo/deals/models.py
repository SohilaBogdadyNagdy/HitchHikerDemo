from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from ..trips.models import Trip
from ..shipments.models import Shipment


class Deal(models.Model):
    """

    """
    shipment_id = models.ForeignKey(Shipment, on_delete=models.CASCADE)
    trip_id = models.ForeignKey(Trip, on_delete=models.CASCADE)
    cost = models.IntegerField(_("Transfer Cost"))
    is_traveler_confirmed = models.BooleanField(default=False)
    is_shipper_confirmed = models.BooleanField(default=False)
