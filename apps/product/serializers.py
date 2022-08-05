from rest_framework import serializers
# from rest_framework.response import Response


from apps.product.models import *
from apps.user.models import User

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['date','name','category','price','image','description','user']
        read_only_fields=('user',)

    def create(self, validated_data):
        pr = Product.objects.filter(user = validated_data.get('user'))
        if len(pr) < 3:
            return Product.objects.create(**validated_data)


class SendSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['description',]
\

    