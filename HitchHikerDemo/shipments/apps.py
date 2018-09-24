from django.apps import AppConfig


class ShipmentsAppConfig(AppConfig):

    name = "HitchHikerDemo.shipment"
    verbose_name = "shipment"

    def ready(self):
        try:
            import shipment.signals  # noqa F401
        except ImportError:
            pass
