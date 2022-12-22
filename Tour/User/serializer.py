from rest_framework import serializers
from User.models import user
class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username= serializers.CharField(max_length=100)
    email= serializers.CharField(max_length=100)
    password= serializers.CharField(max_length=100)
    admin= serializers.BooleanField()
    createdAt= serializers.DateTimeField()
    updatedAt= serializers.DateTimeField()

    def create(self, data):
        return user.objects.create(**data)