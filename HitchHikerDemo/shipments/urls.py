from rest_framework import routers

from .views import ShipmentViewSet

app_name = "shipment"
router = routers.DefaultRouter()
router.register(r'', ShipmentViewSet, base_name='Shipment')

urlpatterns = router.urls
