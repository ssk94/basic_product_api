from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.serializers import *
from app.models import *
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

# Create your views here.
class Login_Api(APIView):
    serializer_class = user_serializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            username = serializer.data['username']
            password = serializer.data['password']
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                token = Token.objects.get(user=user)
                return Response({'token':token.key},
                status=status.HTTP_200_OK)
            else:
                return Response({'message':"invalide user"},
                status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Product_Api(APIView):
    serializer_class = product_serializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.data['name']
            description = serializer.data['description']
            type = serializer.data['type']

            product_obj = Product(
                name = name,
                description=description,
            )

            if type == 'Mobile' or type == 'mobile':
                product_obj.type = 'Mobile'
                product_obj.processor = serializer.data['processor']
                product_obj.ram = serializer.data['ram']
                product_obj.screen_size = serializer.data['screen_size']
                product_obj.color = serializer.data['color']
                product_obj.save()
            else:
                product_obj.type = 'Laptop'
                product_obj.processor = serializer.data['processor']
                product_obj.ram = serializer.data['ram']
                product_obj.hd_capacity = serializer.data['hd_capacity']
                product_obj.save()

            return Response({"message":"saved"},
            status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):
        slug = request.GET.get('type')
        if slug == "Mobile" or slug == "mobile":
            products = Product.objects.filter(type='Mobile')
            serializer = Product_list_mobile_serializer(products,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        elif slug == "Laptop" or slug == "laptop":
            products = Product.objects.filter(type='Laptop')
            serializer = Product_list_laptop_serializer(products,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            products = Product.objects.all()
            serializer = Product_list(products,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self, request, id):
        type_ = request.GET.get('type')
        products = Product.objects.get(id=id)
        products.name = request.data[0]["name"]
        products.description = request.data[0]["description"]
        if type_ == 'mobile' or type_ == 'Mobile': 
            products.type = request.data[0]["type"]
            products.processor = request.data[0]["processor"]
            products.ram = request.data[0]["ram"]
            products.screen_size = request.data[0]["screen_size"] 
            products.color = request.data[0]["color"]
            products.save()
        else:
            products.type = request.data[0]["type"]
            products.processor = request.data[0]["processor"]
            products.ram = request.data[0]["ram"]
            products.screen_size = request.data[0]["screen_size"] 
            products.hd_capacity = request.data[0]["hd_capacity"] 
            products.save()
            
        content = {'message':'updated'}
        return Response(content,status=status.HTTP_200_OK)


    def delete(self, request, id):
        products = Product.objects.get(id=id)
        content = {'message':'deleted'}
        products.delete()
        return Response(content,status=status.HTTP_200_OK)

            



