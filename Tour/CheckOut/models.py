from django.db import models

# Create your models here.
class CheckOut(models.Model):
    number_adult= models.IntegerField(default=0)
    number_children= models.IntegerField(default=0)
    number_baby= models.IntegerField(default=0)
    payment_methods= models.IntegerField(default=0)
    name= models.CharField(max_length=255)
    phoneNumber= models.IntegerField(default=0)
    email= models.CharField(max_length=255)
    total= models.IntegerField(default=0)
    tour_code= models.CharField(max_length=255)
    createdAt= models.DateTimeField(blank=True)
    updatedAt= models.DateTimeField(blank=True)
