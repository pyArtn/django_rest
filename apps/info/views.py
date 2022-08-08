from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from apps.info.models import *
from apps.info.serializers import *
from apps.info.service import ActiveFilter 
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

# Create your views here.


class ActiveView(generics.ListAPIView):
    queryset = Active.objects.all()
    serializer_class = ActiveSerializer



class ActiveAllListView(generics.ListAPIView):
    queryset = ActiveList.objects.all()
    serializer_class = ActiveListSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_class = ActiveFilter
    ordering_fields = ['date', 'int']





