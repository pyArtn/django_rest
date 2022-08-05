from rest_framework.routers import DefaultRouter

from apps.posts.views import PostViewSet, PostImageViewSet

router = DefaultRouter()
router.register(
    prefix='posts',
    viewset=PostViewSet
)
router.register(
    prefix='post_image',
    viewset=PostImageViewSet
)

urlpatterns = router.urls
