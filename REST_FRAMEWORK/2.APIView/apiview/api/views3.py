from functools import partial
from .serializers import StudentSerializer
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from rest_framework.views import APIView

#-------------- FUNCTION BASED API VIEW----------

@api_view(['GET','POST','PUT','DELETE'])
def get_student(request):
    if request.method == 'GET':
        id = request.data.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu)
        return Response(serializer.data)
    if request.method=='POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save
            res = {'msg':'data created successfully'}
            return Response(res)
        return Response(serializer.errors)
    if request.method=='PUT':
        id = request.data.get(id)
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'data updated successfully'}
            return Response(res)
    if request.method=='PATCH':
        id = request.data.get(id)
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'data updated successfully'}
            return Response(res)
    if request.method=='DELETE':
        id = request.data.get(id)
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response({'msg':'data deleted successfully'})

