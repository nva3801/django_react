from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from CategoryList.models import CategoryList
from CategoryList.serializer import CategoryListSerializer
# Create your views here.
@api_view(['GET'])
def cate_list1(request):
    categories_list= CategoryList.objects.all()
    serializer= CategoryListSerializer(categories_list, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def catelist_create(request):
    serilizer= CategoryListSerializer(data=request.data)
    if serilizer.is_valid():
        serilizer.save()
        return Response(serilizer.data , status=status.HTTP_200_OK)
    else:
        return Response(serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def categorylist(request,pk):
    categorylist=CategoryList.objects.get(pk=pk)
    if request.method =='GET':
        serializer= CategoryListSerializer(categorylist)
        return Response(serializer.data , status=status.HTTP_200_OK)

    if request.method =='PUT':
        serializer= CategoryListSerializer(categorylist, data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
    if request.method =='DELETE':
        categorylist.delete()
        return Response({'delete success': True}, status=status.HTTP_200_OK)