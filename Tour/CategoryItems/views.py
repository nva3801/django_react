from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from CategoryItems.models import CategoryItem
from CategoryItems.serializer import CategoryItemSerializer
# Create your views here.
@api_view(['GET'])
def cateitem_list(request):
    categoryitems= CategoryItem.objects.all()
    serializer= CategoryItemSerializer(categoryitems, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def cateitem_create(request):
    serilizer= CategoryItemSerializer(data=request.data)
    if serilizer.is_valid():
        serilizer.save()
        return Response(serilizer.data , status=status.HTTP_200_OK)
    else:
        return Response(serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def categoryitem(request,pk):
    categoryitem=CategoryItem.objects.get(pk=pk)
    if request.method =='GET':
        serializer= CategoryItemSerializer(categoryitem)
        return Response(serializer.data , status=status.HTTP_200_OK)

    if request.method =='PUT':
        serializer= CategoryItemSerializer(categoryitem, data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
    if request.method =='DELETE':
        categoryitem.delete()
        return Response({'delete success': True}, status=status.HTTP_200_OK)