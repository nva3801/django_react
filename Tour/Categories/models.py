from django.db import models

# Create your models here.
class Category(models.Model):
    title= models.CharField(max_length=255)
    slug= models.CharField(max_length=255)
    createdAt= models.DateTimeField(blank=True)
    updatedAt= models.DateTimeField(blank=True)