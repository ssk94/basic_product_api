from rest_framework import serializers
from app.models import *

class user_serializer(serializers.Serializer):
    username = serializers.CharField(max_length=250)
    password = serializers.CharField(
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

class product_serializer(serializers.Serializer):
    name = serializers.CharField(max_length=300)
    description = serializers.CharField(max_length=300)
    type = serializers.CharField(max_length=20)
    processor = serializers.CharField(max_length=20,required=False)
    ram = serializers.CharField(max_length=20,required=False)
    screen_size = serializers.CharField(max_length=20,required=False)
    color = serializers.CharField(max_length=20,required=False)
    hd_capacity = serializers.CharField(max_length=20,required=False)

class Product_list(serializers.ModelSerializer):
    class Meta():
        model = Product
        fields = '__all__'

class Product_list_mobile_serializer(serializers.ModelSerializer):
    class Meta():
        model = Product
        exclude = ('hd_capacity', )

class Product_list_laptop_serializer(serializers.ModelSerializer):
    class Meta():
        model = Product
        exclude = ('color','screen_size', )


