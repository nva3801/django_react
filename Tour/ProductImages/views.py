from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from ProductImages.models import ProductImage
from ProductImages.serializer import ProductImageSerializer
# Create your views here.
@api_view(['GET'])
def productimg_list(request):
    productimgs= ProductImage.objects.all()
    serializer= ProductImageSerializer(productimgs, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def productimg_create(request):
    serilizer= ProductImageSerializer(data=request.data)
    if serilizer.is_valid():
        serilizer.save()
        return Response(serilizer.data , status=status.HTTP_200_OK)
    else:
        return Response(serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def productimg(request,pk):
    productimg=ProductImage.objects.get(pk=pk)
    if request.method =='GET':
        serializer= ProductImageSerializer(productimg)
        return Response(serializer.data , status=status.HTTP_200_OK)

    if request.method =='PUT':
        serializer= ProductImageSerializer(productimg, data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
    if request.method =='DELETE':
        productimg.delete()
        return Response({'delete success': True}, status=status.HTTP_200_OK)