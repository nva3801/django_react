from django.db import models

# Create your models here.
class ProductImage(models.Model):
    product_id= models.CharField(max_length=255)
    image= models.CharField(max_length=255)
    createdAt= models.DateTimeField(blank=True)
    updatedAt= models.DateTimeField(blank=True)