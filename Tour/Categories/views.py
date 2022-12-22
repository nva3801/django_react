from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from Categories.models import Category
from Categories.serializer import CategorySerializer
# Create your views here.
@api_view(['GET'])
def cate_list(request):
    categories= Category.objects.all()
    serializer= CategorySerializer(categories, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def cate_create(request):
    serilizer= CategorySerializer(data=request.data)
    if serilizer.is_valid():
        serilizer.save()
        return Response(serilizer.data , status=status.HTTP_200_OK)
    else:
        return Response(serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def category(request,pk):
    category=Category.objects.get(pk=pk)
    if request.method =='GET':
        serializer= CategorySerializer(category)
        return Response(serializer.data , status=status.HTTP_200_OK)

    if request.method =='PUT':
        serializer= CategorySerializer(category, data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
    if request.method =='DELETE':
        category.delete()
        return Response({'delete success': True}, status=status.HTTP_200_OK)