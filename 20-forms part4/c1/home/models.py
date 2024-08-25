from django.db import models


# Create your models here.


class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    country = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField(default=26)
    city = models.CharField(max_length=200, default='Tehran')


