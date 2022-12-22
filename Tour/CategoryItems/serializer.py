from rest_framework import serializers
from CategoryItems.models import CategoryItem
class CategoryItemSerializer(serializers.Serializer):
    id= serializers.ReadOnlyField()
    title= serializers.CharField(max_length=255)
    slug= serializers.CharField(max_length=255)
    description= serializers.CharField(max_length=255)
    category_id = serializers.CharField(max_length=255)
    image= serializers.CharField(max_length=255)
    createdAt= serializers.DateTimeField()
    updatedAt= serializers.DateTimeField()

    def create(self, data):
        return CategoryItem.objects.create(**data)

    def update(self, instance, data):
        instance.title=data.get('title', instance.title)
        instance.slug=data.get('slug', instance.slug)
        instance.description=data.get('description', instance.description)
        instance.category_id=data.get('category_id', instance.category_id)
        instance.image=data.get('image', instance.image)
        instance.createdAt=data.get('createdAt', instance.createdAt)
        instance.updatedAt=data.get('updatedAt', instance.updatedAt)

        instance.save()
        return instance