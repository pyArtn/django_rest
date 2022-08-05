from rest_framework import viewsets
from rest_framework.response import Response
from apps.product.models import Product
from apps.product.serializers import ProductSerializer, SendSerializer
from send_tg import send_telegram
from rest_framework import generics, status

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

    def perform_create(self, serializer):
        serializer.validated_data['user'] = self.request.user
        return serializer.save()


    # def create(self, request, *args, **kwargs):
    #     list = Product.objects.filter(user = self.request.user)
    #     if len(list) < 3:
    #         serializer = self.get_serializer(data=request.data)
    #         serializer.is_valid(raise_exception=True)
    #         self.perform_create(serializer)
    #         headers = self.get_success_headers(serializer.data)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    #     else:
    #         return Response({'Error':'Больше 3 раза нельзя'})


    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except AssertionError:
            return Response({'Error':'добавлять больше 3 продуктов нельзя'})


class SendTg(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = SendSerializer

    def post(self, request, *args, **kwargs):
        send_telegram(request.data.get('description'))
        return Response({'Error':'сообшение отправлено'})




