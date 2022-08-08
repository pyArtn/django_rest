from rest_framework import serializers
from apps.info.models import *
# from rest_framework.response import Response


from apps.product.models import *

class ActiveSerializer(serializers.ModelSerializer):
    class Meta:
        model=Active
        fields=['all', 'today']

class ActiveListSerializer(serializers.ModelSerializer):
    class Meta:
        model=ActiveList
        fields=['date', 'int']



    