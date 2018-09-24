from django.apps import AppConfig


class DealsAppConfig(AppConfig):

    name = "HitchHikerDemo.deals"
    verbose_name = "Trips"

    def ready(self):
        try:
            import deals.signals  # noqa F401
        except ImportError:
            pass
