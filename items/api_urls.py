from rest_framework.routers import DefaultRouter
from items.api_views import ItemViewSet

router = DefaultRouter()

router.register(
    "items",
    ItemViewSet,
    basename="item"
)

urlpatterns = router.urls