from django.db import models

# Create your models here.
class TourCode(models.Model):
    product_id= models.CharField(max_length=255)
    tour_code= models.CharField(max_length=255)
    start= models.DateField(default=None)
    end= models.DateField(default=None)
    price_adult= models.IntegerField(default=0)
    price_children= models.IntegerField(default=0)
    price_baby= models.IntegerField(default=0)
    createdAt= models.DateTimeField(blank=True)
    updatedAt= models.DateTimeField(blank=True)