from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from CheckOut.models import CheckOut
from CheckOut.serializer import CheckOutSerializer
# Create your views here.
@api_view(['GET'])
def checkout_list(request):
    checkouts= CheckOut.objects.all()
    serializer= CheckOutSerializer(checkouts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def checkout_create(request):
    serilizer= CheckOutSerializer(data=request.data)
    if serilizer.is_valid():
        serilizer.save()
        return Response(serilizer.data , status=status.HTTP_200_OK)
    else:
        return Response(serilizer.errors, status=status.HTTP_400_BAD_REQUEST)
