from django.db import models
from django.contrib.postgres.fields import ArrayField

from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class Shipment(models.Model):
    """

    """
    title = models.CharField(_("Shipment type"), blank=False, max_length=255)
    image = models.ImageField(_("Shipment photo"))
    weight = models.IntegerField(_("Shipment weight KG"))
    height_dimesion = models.IntegerField(_("height"))
    width_dimesion = models.IntegerField(_("width"))
    is_delivered = models.CharField(_("is_delivered"), blank=False, max_length=255)

