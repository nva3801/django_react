from rest_framework import serializers
from Product.models import Product
class ProductSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title= serializers.CharField(max_length=255)
    slug= serializers.CharField(max_length=255)
    description= serializers.CharField(max_length=255)
    category_id= serializers.CharField(max_length=255)
    image= serializers.CharField(max_length=255)
    time= serializers.CharField(max_length=255)
    vehicle= serializers.CharField(max_length=255)
    starting_point= serializers.CharField(max_length=255)
    destination= serializers.CharField(max_length=255)
    tour= serializers.CharField(max_length=255)
    tour_policy= serializers.CharField(max_length=255)
    price= serializers.IntegerField()
    tour_code= serializers.CharField(max_length=255)
    product_image= serializers.CharField(max_length=255)
    createdAt= serializers.DateTimeField()
    updatedAt= serializers.DateTimeField()

    def create(self, data):
        return Product.objects.create(**data)

    def update(self, instance, data):
        instance.title=data.get('title', instance.title)
        instance.slug=data.get('slug', instance.slug)
        instance.description=data.get('description', instance.description)
        instance.category_id=data.get('category_id', instance.category_id)
        instance.image=data.get('image', instance.image)
        instance.time=data.get('time', instance.time)
        instance.vehicle=data.get('vehicle', instance.vehicle)
        instance.starting_point=data.get('starting_point', instance.starting_point)
        instance.destination=data.get('destination', instance.destination)
        instance.tour=data.get('tour', instance.tour)
        instance.tour_policy=data.get('tour_policy', instance.tour_policy)
        instance.price=data.get('price', instance.price)
        instance.tour_code=data.get('tour_code', instance.tour_code)
        instance.product_image=data.get('product_image', instance.product_image)
        instance.createdAt=data.get('createdAt', instance.createdAt)
        instance.updatedAt=data.get('updatedAt', instance.updatedAt)

        instance.save()
        return instance