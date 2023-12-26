from functools import partial
from .serializers import UserSerializer
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .models import User,Order
import base64 
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
import jwt
import json
from django.forms.models import model_to_dict


jwt_key = "mhasecret"


@api_view(['POST'])
def myorders(request):
    token = request.data.get('token')
    print(token)
    decoded = jwt.decode(token, jwt_key, algorithms=["HS256"])
    print(decoded)
    orders_query = Order.objects.filter(email=decoded['email'],status='Paid')
    orders = []
    for item in orders_query:
        orders.append(model_to_dict(item))
    print(orders)
    return Response({"orders":orders})

@api_view(['POST'])
def order(request):
    orderId = request.data.get('id')
    myorder = Order.objects.get(orderId=orderId)

    return Response({"order":model_to_dict(myorder)})


@api_view(['POST'])
def pincode(request):
    return
