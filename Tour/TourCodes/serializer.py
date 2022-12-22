from rest_framework import serializers
from TourCodes.models import TourCode
class TourCodeSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    product_id= serializers.CharField(max_length=255)
    tour_code= serializers.CharField(max_length=255)
    start= serializers.DateField(default=None)
    end= serializers.DateField(default=None)
    price_adult= serializers.IntegerField(default=0)
    price_children= serializers.IntegerField(default=0)
    price_baby= serializers.IntegerField(default=0)
    createdAt= serializers.DateTimeField()
    updatedAt= serializers.DateTimeField()
    def create(self, data):
        return TourCode.objects.create(**data)

    def update(self, instance, data):
        instance.product_id=data.get('product_id', instance.product_id)
        instance.tour_code=data.get('tour_code', instance.tour_code)
        instance.start=data.get('start', instance.start)
        instance.end=data.get('end', instance.end)
        instance.price_adult=data.get('price_adult', instance.price_adult)
        instance.price_children=data.get('price_children', instance.price_children)
        instance.price_baby=data.get('price_baby', instance.price_baby)
        instance.createdAt=data.get('createdAt', instance.createdAt)
        instance.updatedAt=data.get('updatedAt', instance.updatedAt)

        instance.save()
        return instance