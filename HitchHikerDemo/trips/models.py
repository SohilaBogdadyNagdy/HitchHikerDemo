from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class Trip(models.Model):
    """

    """
    from_country = models.CharField(_("Trip location Country"), max_length=30)
    to_country = models.CharField(_("Trip Destination Country"),  max_length=30)
    from_city = models.CharField(_("Trip location City"), max_length=30)
    to_city = models.CharField(_("Trip Destination City"),  max_length=30)
    departure_time = models.DateTimeField(_("Departure Time"))

