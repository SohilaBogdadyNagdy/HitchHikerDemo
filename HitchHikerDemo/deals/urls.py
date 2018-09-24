from rest_framework import routers

from .views import DealViewSet

app_name = "deals"
router = routers.DefaultRouter()
router.register(r'', DealViewSet, base_name='Deal')

urlpatterns = router.urls
