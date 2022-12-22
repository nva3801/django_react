from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from TourCodes.models import TourCode
from TourCodes.serializer import TourCodeSerializer
# Create your views here.
@api_view(['GET'])
def tourcode_list(request):
    tourcodes= TourCode.objects.all()
    serializer= TourCodeSerializer(tourcodes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def tourcode_create(request):
    serilizer= TourCodeSerializer(data=request.data)
    if serilizer.is_valid():
        serilizer.save()
        return Response(serilizer.data , status=status.HTTP_200_OK)
    else:
        return Response(serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def tourCode(request,pk):
    tourCode=TourCode.objects.get(pk=pk)
    if request.method =='GET':
        serializer= TourCodeSerializer(tourCode)
        return Response(serializer.data , status=status.HTTP_200_OK)

    if request.method =='PUT':
        serializer= TourCodeSerializer(tourCode, data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
    if request.method =='DELETE':
        tourCode.delete()
        return Response({'delete success': True}, status=status.HTTP_200_OK)