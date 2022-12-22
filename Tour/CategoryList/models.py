from django.db import models

# Create your models here.
class CategoryList(models.Model):
    title= models.CharField(max_length=255)
    slug= models.CharField(max_length=255)
    category_id= models.IntegerField()
    categoryItem= models.CharField(max_length=255)
    createdAt= models.DateTimeField(blank=True)
    updatedAt= models.DateTimeField(blank=True)