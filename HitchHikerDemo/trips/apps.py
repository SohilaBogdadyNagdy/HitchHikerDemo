from django.apps import AppConfig


class TripsAppConfig(AppConfig):

    name = "HitchHikerDemo.trips"
    verbose_name = "Trips"

    def ready(self):
        try:
            import trips.signals  # noqa F401
        except ImportError:
            pass
