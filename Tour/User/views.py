from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from User.models import user
from User.serializer import UserSerializer
# Create your views here.
@api_view(['GET'])
def user_list(request):
    users= user.objects.all()
    serilizer = UserSerializer(users, many=True)
    return Response(serilizer.data)

@api_view(['POST'])
def user_create(request):
    serilizer= UserSerializer(data=request.data)
    if serilizer.is_valid():
        serilizer.save()
        return Response(serilizer.data)
    else:
        return Response(serilizer.errors)
