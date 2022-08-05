from django.urls import path
from apps.info.views import *



urlpatterns = [
    path('', ActiveAllListView.as_view()),
    path('today/', ActiveView.as_view()),


]