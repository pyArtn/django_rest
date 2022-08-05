from rest_framework.routers import DefaultRouter

from apps.users.views import UserViewSet

router = DefaultRouter()
router.register(
    prefix='',
    viewset=UserViewSet
)

urlpatterns = router.urls
