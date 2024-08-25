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


class Test(models.Model):
    name = models.CharField(max_length=29)


class Product(models.Model):
    STATUS_CHOICES = [
        ('1', 'in stock'),
        ('2', 'out of stock')
    ]
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70)
    description = models.TextField()
    price = models.CharField(help_text="قیمت محصولات", default="20000000")
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, verbose_name='وضعیت')
    created_at = models.DateTimeField(auto_now_add=True,)
    update_at = models.DateTimeField(auto_now=True)

