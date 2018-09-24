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
    dimension = ArrayField(ArrayField(models.IntegerField())) # For height and width
    is_delivered = models.CharField(_(""), blank=False, max_length=255)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
