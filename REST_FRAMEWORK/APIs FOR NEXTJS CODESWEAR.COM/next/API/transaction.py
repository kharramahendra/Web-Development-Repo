from functools import partial
from sre_parse import State
from .serializers import UserSerializer
from django.shortcuts import render,redirect
from rest_framework import serializers
from rest_framework.response import Response
from .models import Product, User,Order
import base64
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
import jwt
import requests
import json


import razorpay
from next.settings import RAZORPAY_API_KEY,RAZORPAY_API_SECRET_KEY

client = razorpay.Client(auth=(RAZORPAY_API_KEY,RAZORPAY_API_SECRET_KEY))
@api_view(['POST'])
def pretransaction(request):
    if request.method == "POST":
        name=request.data.get('name')
        phone=request.data.get('phone')
        email=request.data.get('email')
        address=request.data.get('address')
        pincode=request.data.get('pincode')
        phone = request.data.get('phone')
        amount = request.data.get('subTotal')
        oid = request.data.get('oid')
        city=request.data.get('city')
        state=request.data.get('state')
        products = request.data.get('cart')



        # ALL CHECKS FOR ORDER PLACEMENT----------------------------------------------------------------------------

        # check if cart temporred
        # check if cart is empty
        if request.data.get('subTotal')<=0:
            return Response({'success':False,"error":"Please build your cart and try again!",'clear':True})

        # check if cart temporred
        sumTotal = 0
        for item in request.data.get('cart'):
            sumTotal+=request.data.get('cart')[item]['price']*request.data.get('cart')[item]['qty']
            product = Product.objects.get(slug=item)
            # check if any product in cart is out of stock
            if product.availableQty<request.data.get('cart')[item]['qty']:
                return Response({"success":False,"error":"Some items in your cart went out of stock.Please try again","clear":True})
            if product.price != request.data.get('cart')[item]['price']:
                return Response({"success":False, 'error':"The price of some items in your cart has changed.Please try again","clear":True})
        if sumTotal!=request.data.get('subTotal'):
            return Response({"success":False, 'error':"The price of some items in your cart has changed.Please try again","clear":True})
        # check if details are valid or not
        if not len(request.data.get('phone'))==10 or not int(request.data.get('phone')):
            return Response({"success":False,"error":"Please enter your 10 digit Phone number!","clear":False})
        if not len(request.data.get('pincode'))==6 or not int(request.data.get('pincode')):
            return Response({"success":False,"error":"Please enter your 6 digit Pincode!","clear":False})
        
        #-----------------------------------------------------------------------------------------------------------




        #----SAVE THE ORDER ----------------------------------------------------
        order = Order(email=email,name=name,orderId=oid,address=address,phone=phone,city=city,state=state,pincode=pincode,amount=amount,products=products)
        order.save()
        #-----------------------------------------------------------------------




        callback_url = 'https://127.0.0.1/posttransaction/'

        #### ----------RAZORPAY------------------------------------------
        DATA = {
        "amount": request.data.get('subTotal')*100,
        "currency": "INR",
        "receipt": "captured",
        "notes": {
            "key1": "value3",
            "key2": "value2"
        }
        }
        payment_order = client.order.create(data=DATA)
        payment_order_id = payment_order['id']
        print("47")
        context = {
            'amount':amount,
            'api_key':RAZORPAY_API_KEY,
            'order_id':payment_order_id,
            "currency": "INR",
            'user_name':name,
            'user_phone':phone,
            'user_email':email,
            'callback_url':callback_url,
            'address':address,
            'city':request.data.get('city'),
            'pincode':pincode
        }
        return Response({"success":True,"context":context})





@api_view(['POST'])
def posttransaction(request):
    if request.method == "POST":
        try:
            oid = request.data.get('oid')
            pid = request.data.get('pid')
            poid = request.data.get('poid')
            psign = request.data.get('psign')
            params_dict = {
            'razorpay_order_id': poid,
            'razorpay_payment_id': pid,
            'razorpay_signature': psign
            }
            result = client.utility.verify_payment_signature(params_dict)
            if result==None or result == True:
                order = Order.objects.get(orderId=oid)
                order.status = 'Paid'
                order.deliveryStatus = 'Shipped'
                order.transactionid = pid
                order.save()
                return Response({'success':True,"payment":"successfull",})
            else:
                return Response({"success":False})
        except:
            return Response({"success":False,"error":"some error occured"})