# from django.db import models
from shoppingCart.models import Orders,Products,Orders_items
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['title' ,
                    'description' ,
                    'price' ,
                    'created_At' ,
                  'updated_At','image']



class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = [
            'user_id','total','products','created_At','updated_At','status','mode_of_payment'
        ]
        depth =1

class Order_items_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Orders_items
        fields = [
            'order_id','product_id','Quantity','price'
        ]



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user