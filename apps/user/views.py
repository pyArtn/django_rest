from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from apps.user.models import User
from apps.user.permissions import *
from apps.user.serializers import UserSerializerList, UserSerializers




class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = (UpdateProfile,)
    

    def get_serializer_class(self):
        if self.action in ['list', 'retrive']:
            return UserSerializerList
        return UserSerializers

    def get_permissions_(self):
        return super().get_permissions()



    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())


        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    

    
