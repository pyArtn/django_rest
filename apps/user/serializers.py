from rest_framework import serializers
# from rest_framework.response import Response
from apps.user.models import User

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','avatar','password']

    def create(self, validated_data):
        password = validated_data['password']
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user
    
class UserSerializerList(serializers.ModelSerializer):
     class Meta:
        model=User
        fields=['username','last_action','avatar']
