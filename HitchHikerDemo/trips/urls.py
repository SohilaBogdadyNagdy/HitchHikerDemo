from django.conf.urls import url
from rest_framework import routers

from .views import TripsViewSet

app_name = "trips"
router = routers.DefaultRouter()
router.register(r'all', TripsViewSet, base_name='Trip')

urlpatterns = router.urls
