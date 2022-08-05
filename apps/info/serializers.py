from rest_framework import serializers
from apps.info.models import *
# from rest_framework.response import Response


from apps.product.models import *

class ActiveSerializer(serializers.ModelSerializer):
    class Meta:
        model=Active
        fields=['all', 'today']

class ActiveAllSerializer(serializers.ModelSerializer):
    class Meta:
        model=ActiveAll
        fields=['date', 'int']



    