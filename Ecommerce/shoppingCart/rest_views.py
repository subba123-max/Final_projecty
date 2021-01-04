from django.contrib.auth.models import User
from rest_framework.authentication import  TokenAuthentication
from rest_framework import  viewsets
from rest_framework.permissions import IsAuthenticated
from shoppingCart.models import Orders,Products,Orders_items
from shoppingCart.serializers import UserSerializer,ProductSerializer,OrdersSerializer,Order_items_Serializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProductViewset(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class OrdersViewset(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class Order_item_Viewset(viewsets.ModelViewSet):
    queryset = Orders_items.objects.all()
    serializer_class = Order_items_Serializer
    authentication_classes =  [TokenAuthentication]
    permission_classes = [IsAuthenticated]