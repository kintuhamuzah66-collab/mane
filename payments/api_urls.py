from rest_framework.routers import DefaultRouter
from payments.api_views import PaymentViewSet

router = DefaultRouter()

router.register(
    "payments",
    PaymentViewSet,
    basename="payment"
)

urlpatterns = router.urls