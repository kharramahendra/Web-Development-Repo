from asyncio import streams
from functools import partial
from .serializers import StudentSerializer
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .models import Student
from rest_framework.renderers import JSONRenderer


#@api_view() # by default get method is called
#def student_api(request):
#    return Response({'msg':'hello world'})

## function based api view

## ---------- AUTHENTICATION AND PERMISSIONS -----------------------------------+
from rest_framework.authentication import BasicAuthentication,SessionAuthentication              #   |
from rest_framework.permissions import IsAuthenticated,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly,IsAuthenticatedOrReadOnly,AllowAny,IsAdminUser #   |
## DJANGOMODELPERMISSIONs - GIVE PERMISSIONS TO USER AS PER DJANGO USER SYSTEM (authenticataed is complesery)
## DjangoModelPermissionsOrAnonReadOnly - unauthenticated users also have permission of getting data



@api_view(['POST','GET','PUT','PATCH','DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def student_api(request):
    if request.method == 'GET':
        id = request.data.get('id')
        if id is not None:
            stu = Student.objects.get(id = id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu,many = True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created'})
        return Response(serializer.errors)
    
    if request.method == 'PUT':
        id = request.data.get('id')
        stu = Student.objects.get(id = id)
        serializer = StudentSerializer(stu, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data updated put request'})
        return Response(serializer.errors)
    
    if request.method == 'PATCH':
        id = request.data.get('id')
        stu = Student.objects.get(id = id)
        serializer = StudentSerializer(stu, data = request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data updated patch request'})
        return Response(serializer.errors)
    
    if request.method == 'DELETE':
        id = request.data.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response({'msg':'data deleted'})


##------------SERIALISATION------------------
# stu = Student.objects.filter(age=20) #complex query set or model instase
# serializer = StudentSerializer(stu) #python object data type
# json_data = JSONRenderer().render(serializer)#json data for frontend
#-------------------------------------------


##-----------DESRIALISATION------------------
# json_data = request.body
# stream = io.BiosIo(json_data)
# python_data = JSONparser().parse(stream)
# serializer = StudentSerializer(data=python_data)
# if serializer.is_valid():
#     res = {'msg':'successful'}
#     json_res = JSONRenderer().render(res)
#     return response(json_res)
#--------------------------------------------




# StudentSerializer(stu) #converts complex data type into python object type
# StudentSerializer(data=request.data)#converts python data type into complex data type
# StudentSerializer(stu,data=request.data)#PUT request
# StudentSerializer(stu,data=request.data,partial=True)#PATCH request





