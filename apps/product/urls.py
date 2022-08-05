from rest_framework import routers
from django.urls import path
from .views import ProductViewSet, SendTg


router=routers.DefaultRouter()
router.register('',ProductViewSet)

urlpatterns = [
    path('send/', SendTg.as_view()),

]

urlpatterns+=router.urls