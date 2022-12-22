from rest_framework import serializers
from ProductImages.models import ProductImage
class ProductImageSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    product_id= serializers.CharField(max_length=255)
    image= serializers.CharField(max_length=255)
    createdAt= serializers.DateTimeField()
    updatedAt= serializers.DateTimeField()

    def create(self, data):
        return ProductImage.objects.create(**data)

    def update(self, instance, data):
        instance.product_id=data.get('product_id', instance.product_id)
        instance.image = data.get('image', instance.image)
        instance.createdAt=data.get('createdAt', instance.createdAt)
        instance.updatedAt=data.get('updatedAt', instance.updatedAt)

        instance.save()
        return instance