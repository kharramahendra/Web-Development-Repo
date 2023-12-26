from functools import partial
from .serializers import StudentSerializer
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from rest_framework.views import APIView

## ---------------CLASS BASED API VIEW----------------------

class StudentAPI(APIView):
    def get(self,request,pk=None,format=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id = id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu,many = True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created'})
        return Response(serializer.errors)
    
    def put(self,request,pk,format=None):
        id = pk
        stu = Student.objects.get(id = id)
        serializer = StudentSerializer(stu, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data updated put request'})
        return Response(serializer.errors)
    
    def patch(self,request,pk,format=None):
        id = pk
        stu = Student.objects.get(id = id)
        serializer = StudentSerializer(stu, data = request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data updated patch request'})
        return Response(serializer.errors)

    def delete(self,request,pk,format=None):
        id = pk
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response({'msg':'data deleted'})