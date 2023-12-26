from functools import partial

from django.http.response import JsonResponse
from .serializers import StudentSerializer
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from rest_framework.views import APIView
from rest_framework import viewsets


class StudentViewSet(viewsets.ViewSet):
    def list(self,request):
        stu = Student.objects.all()
        serializer = StudentSerializer(stu,many = True)
        return Response(serializer.data)
    
    def create(self,request,format=None):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created'})
        return Response(serializer.errors)
    
    def retrieve(self,request,pk=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
    
    def update(self,request,pk):
        id = pk
        stu = Student.objects.get(id = id)
        serializer = StudentSerializer(stu, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data updated'})
        return Response(serializer.errors)

    def partial_update(self,request,pk):
        id = pk
        stu = Student.objects.get(id = id)
        serializer = StudentSerializer(stu, data = request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data updated patch request'})
        return Response(serializer.errors)

    def destroy(self,request,pk):
        id = pk
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response({'msg':'data deleted'})