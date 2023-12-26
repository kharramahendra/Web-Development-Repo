from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework import viewsets
from rest_framework.generics import ListAPIView

from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination
## LimitOffsetPagination --> how many number of records their are in a page
from .mypagination import MyPageNumberPagination,MyCursorPagination,MyLimitPagination

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = MyCursorPagination


# ordering for CursorPagination