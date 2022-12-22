from rest_framework import serializers
from Categories.models import Category
class CategorySerializer(serializers.Serializer):
    id= serializers.ReadOnlyField()
    title= serializers.CharField(max_length=255)
    slug= serializers.CharField(max_length=255)
    createdAt= serializers.DateTimeField()
    updatedAt= serializers.DateTimeField()

    class Meta:
        model= Category
    def create(self, data):
        return Category.objects.create(**data)

    def update(self, instance, data):
        instance.title=data.get('title', instance.title)
        instance.slug=data.get('slug', instance.slug)
        instance.createdAt=data.get('createdAt', instance.createdAt)
        instance.updatedAt=data.get('updatedAt', instance.updatedAt)

        instance.save()
        return instance