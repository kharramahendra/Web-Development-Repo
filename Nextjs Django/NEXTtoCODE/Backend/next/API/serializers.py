from django.db.models import fields
from requests.models import ReadTimeoutError
from rest_framework import serializers, validators
from .models import User
from .models import Product

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name','email','phone','password','pincode','address',]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title','slug','desc','img','category','size','color','price','availableQty']
