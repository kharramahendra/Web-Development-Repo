from django.db import models
from jsonfield import JSONField
# Create your models here.

class User(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100,unique=True)
    phone = models.CharField(max_length=100,default="")
    password = models.CharField(max_length=100,default="")
    address = models.CharField(max_length=100,default="")
    pincode = models.CharField(max_length=100,default="")
    def __str__(self):
        return self.email

class Order(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    orderId = models.CharField(max_length=200)
    paymentid = models.CharField(max_length=200,default="")
    paymentInfo = models.CharField(max_length=200,default="",blank=True)
    products = JSONField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    pincode = models.CharField(max_length=6)
    transactionid = models.CharField(max_length=200,default="Not given",blank=True)
    amount = models.CharField(max_length=200)
    status = models.CharField(max_length=100,default='Initiated')
    deliveryStatus = models.CharField(max_length=100,default="unshipped")
    def __str__(self):
        return self.orderId


class Product(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100,unique=True)
    desc = models.CharField(max_length=200)
    img = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    size = models.CharField(max_length=100,blank=True)
    color = models.CharField(max_length=50)
    price = models.IntegerField()
    availableQty = models.IntegerField()
    def __str__(self):
        return self.title + self.slug


class Forgot(models.Model):
    userid = models.CharField(max_length=100)
    email = models.CharField(max_length=100,unique=True)
    token = models.CharField(max_length=200)
    def __str__(self):
        return self.email