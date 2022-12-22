from rest_framework import serializers
from CheckOut.models import CheckOut
class CheckOutSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    number_adult= serializers.IntegerField(default=0)
    number_children= serializers.IntegerField(default=0)
    number_baby= serializers.IntegerField(default=0)
    payment_methods= serializers.IntegerField(default=0)
    name= serializers.CharField(max_length=255)
    phoneNumber= serializers.IntegerField(default=0)
    email= serializers.CharField(max_length=255)
    total= serializers.IntegerField(default=0)
    tour_code= serializers.CharField(max_length=255)
    createdAt= serializers.DateTimeField()
    updatedAt= serializers.DateTimeField()

    def create(self, data):
        return CheckOut.objects.create(**data)
