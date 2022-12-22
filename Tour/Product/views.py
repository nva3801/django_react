from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from Product.models import Product
from Product.serializer import ProductSerializer
# Create your views here.
@api_view(['GET'])
def product_list(request):
    products= Product.objects.all()
    serializer= ProductSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def product_create(request):
    serilizer= ProductSerializer(data=request.data)
    if serilizer.is_valid():
        serilizer.save()
        return Response(serilizer.data , status=status.HTTP_200_OK)
    else:
        return Response(serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def product(request,pk):
    product=Product.objects.get(pk=pk)
    if request.method =='GET':
        serializer= ProductSerializer(product)
        return Response(serializer.data , status=status.HTTP_200_OK)

    if request.method =='PUT':
        serializer= ProductSerializer(product, data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
    if request.method =='DELETE':
        Product.delete()
        return Response({'delete success': True}, status=status.HTTP_200_OK)