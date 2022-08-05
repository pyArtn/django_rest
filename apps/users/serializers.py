from rest_framework import serializers

from apps.users.models import User
from apps.users.tasks import send_message_to_user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'last_activity')


class UserSerializerList(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        send_message_to_user.delay(email=validated_data['email'])
        return user
