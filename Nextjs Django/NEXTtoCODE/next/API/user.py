from functools import partial
from .serializers import UserSerializer
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .models import User
import base64 
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
import jwt
from next.settings import JWT_KEY,CRYPTO_KEY
#AES ECB mode without IV

# encoded_jwt = jwt.encode({"some": "payload"}, "secret", algorithm="HS256")
jwt_key = JWT_KEY
crypto_key = CRYPTO_KEY #Must Be 16 char for AES128

def encrypt(raw):
        raw = pad(raw.encode(),16)
        cipher = AES.new(crypto_key.encode('utf-8'), AES.MODE_ECB)
        return base64.b64encode(cipher.encrypt(raw))

def decrypt(enc):
        enc = base64.b64decode(enc)
        cipher = AES.new(crypto_key.encode('utf-8'), AES.MODE_ECB)
        return unpad(cipher.decrypt(enc),16)


@api_view(['POST','GET','PUT','PATCH','DELETE'])
def signup(request):
    print("api called")
    if request.method == 'POST':
        name = request.data.get('name')
        email = request.data.get('email')
        password = request.data.get('password')
        # print(name,email,password)
        # encrypted = encrypt(password)
        # print(encrypted.decode("utf-8", "ignore"))
        # decrypted=decrypt(encrypted)
        # print("decripted: ",decrypted.decode("utf-8", "ignore"))
        user = User(name=name,email=email,password=encrypt(password).decode("utf-8", "ignore"))
        user.save()
        
        return Response({'success':True})
    else:
        return Response({"success":False})


@api_view(['POST','GET','PUT','PATCH','DELETE'])
def login(request):
    print("api called")
    if request.method == 'POST':
        password = request.data.get('password')
        email = request.data.get('email')
        user = User.objects.filter(email=email)
        if user:
            decrypted_pass = decrypt(user[0].password).decode("utf-8", "ignore")
            print(decrypted_pass)
            print("decrypyed is running")
            if password==decrypted_pass:
                token = jwt.encode({"email":user[0].email,"name":user[0].name}, jwt_key, algorithm="HS256")
                decoded = jwt.decode(token, jwt_key, algorithms=["HS256"])
                print(decoded)
                print(decoded['email'])
                return Response({'success':True,'token':token,'email':user[0].email})
            else:
                return Response({'success':False})
        else:
            return Response({'success':False})
        
        return Response({'success':False})
    else:
        return Response({"success":False})


@api_view(['GET','POST'])
def getuser(request):
    if request.method == 'POST':
        token = request.data.get('token')
        decoded_token = jwt.decode(token, jwt_key, algorithms=["HS256"])
        user = User.objects.filter(email=decoded_token['email'])
        name,email,address,phone,pincode, = user[0].name,user[0].email,user[0].address,user[0].phone,user[0].pincode
        return Response({"name":name,"email":email,"address":address,"pincode":pincode,"phone":phone})
    else:
        return Response({'error':'error'})


@api_view(['POST','GET','PUT'])
def updateuser(request):
    if request.method == 'POST':
        token = request.data.get('token')
        decoded_token = jwt.decode(token, jwt_key, algorithms=["HS256"])
        user = User.objects.get(email=decoded_token['email'])##.update(address=request.data.get('address'),pincode=request.data.get('pincode'),phone=request.data.get('phone'),name=request.data.get('name'))
        user.address=request.data.get('address')
        user.pincode=request.data.get('pincode')
        user.phone=request.data.get('phone')
        user.name=request.data.get('name')
        user.save()
        return Response({"success":True})
    else:
        return Response({'error':'error'})

@api_view(['POST','GET','PUT','PATCH','DELETE'])
def updatepassword(request):
    if request.method == 'POST':
        token = request.data.get('token')
        decoded_token = jwt.decode(token, jwt_key, algorithms=["HS256"])
        user = User.objects.get(email=decoded_token['email'])
        print(user)
        decrypted_pass = decrypt(user.password).decode("utf-8", "ignore")
        print(decrypted_pass,request.data.get('password'))
        if decrypted_pass == request.data.get('password') and request.data.get('npassword') == request.data.get('cpassword'):
            user.password = encrypt(request.data.get('npassword')).decode("utf-8", "ignore")
            # user.update(password=encrypt(request.data.get('npassword')).decode("utf-8", "ignore"))
            user.save()
            return Response({'success':True})
        return Response({'success':False})
    else:
        return Response({'error':'error'})


























@api_view(['POST','GET','PUT','PATCH','DELETE'])
def user_api(request):
    print("API CALLED")
    if request.method == 'GET':
        id = request.data.get('id')
        if id is not None:
            stu = User.objects.get(id = id)
            serializer = UserSerializer(stu)
            return Response(serializer.data)
        stu = User.objects.all()
        serializer = UserSerializer(stu,many = True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = UserSerializer(data = request.data)
        print("BHAI DATA TO AA RHA HAI")
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created'})
        return Response(serializer.errors)
    
    if request.method == 'PUT':
        id = request.data.get('id')
        stu = User.objects.get(id = id)
        serializer = UserSerializer(stu, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data updated put request'})
        return Response(serializer.errors)
    
    if request.method == 'PATCH':
        id = request.data.get('id')
        stu = User.objects.get(id = id)
        serializer = UserSerializer(stu, data = request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data updated patch request'})
        return Response(serializer.errors)
    
    if request.method == 'DELETE':
        id = request.data.get('id')
        stu = User.objects.get(id=id)
        stu.delete()
        return Response({'msg':'data deleted'})