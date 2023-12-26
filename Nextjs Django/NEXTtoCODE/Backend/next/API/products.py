from functools import partial
from .serializers import UserSerializer
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .models import User
from .models import Product
import base64 
from django.forms.models import model_to_dict
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
import jwt
import json

@api_view(['POST','GET','PUT','PATCH','DELETE'])
def getproducts(request):
    cat_tshirts = Product.objects.filter(category='tshirts')
    tshirts = {}
    for item in cat_tshirts:
        print(type(item),item.title)
        if item.title in tshirts:
            if item.color not in tshirts[item.title]['color'] and item.availableQty > 0:
                tshirts[item.title]['color'].append(item.color)
            if item.size not in tshirts[item.title]['size'] and item.availableQty > 0:
                tshirts[item.title]['size'].append(item.size)
        else:
            tshirts[item.title] = model_to_dict(item)# {'title':item.title,'slug':item.slug,'desc':item.desc,'img':item.img,'category':item.category,'size':[],'color':[],'price':item.price,'availableQty':item.availableQty}
            if item.availableQty > 0:
                tshirts[item.title]['color'] = [item.color]
                tshirts[item.title]['size'] = [item.size]
            else:
                tshirts[item.title]['color'] = []
                tshirts[item.title]['size'] = []
    print(tshirts)


    cat_hoodies = Product.objects.filter(category='hoodies')
    hoodies = {}
    for item in cat_hoodies:
        print(type(item),item.title)
        if item.title in hoodies:
            if item.color not in hoodies[item.title]['color'] and item.availableQty > 0:
                hoodies[item.title]['color'].append(item.color)
            if item.size not in hoodies[item.title]['size'] and item.availableQty > 0:
                hoodies[item.title]['size'].append(item.size)
        else:
            hoodies[item.title] = model_to_dict(item)#{'title':item.title,'slug':item.slug,'desc':item.desc,'img':item.img,'category':item.category,'size':[],'color':[],'price':item.price,'availableQty':item.availableQty}
            if item.availableQty > 0:
                hoodies[item.title]['color'] = [item.color]
                hoodies[item.title]['size'] = [item.size]
            else:
                hoodies[item.title]['color'] = []
                hoodies[item.title]['size'] = []
    print(hoodies)
    


    return Response({"tshirts":tshirts,"hoodies":hoodies})



@api_view(['POST','GET','PUT','PATCH','DELETE'])
def getproduct(request):
    if request.method == 'POST':
        req_slug = request.data.get('slug')
        print(req_slug)
        product = Product.objects.get(slug=req_slug)
        product_title = product.title
        print(model_to_dict(product))
        variants = Product.objects.filter(title=product_title)
        print(product,product_title,variants)
        colorSizeSlug = {}
        for item in variants:
            if item.color in colorSizeSlug.keys():
                colorSizeSlug[item.color][item.size] = { 'slug': item.slug }
            else:
                colorSizeSlug[item.color] = {}
                colorSizeSlug[item.color][item.size] = { 'slug': item.slug }
        print(colorSizeSlug)
        return Response({"product":model_to_dict(product),"variants":colorSizeSlug})
  