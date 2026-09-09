from rest_framework.routers import DefaultRouter
from minutes.api_views import MinutesViewSet

router = DefaultRouter()

router.register(
    "minutes",
    MinutesViewSet,
    basename="minutes"
)

urlpatterns = router.urls