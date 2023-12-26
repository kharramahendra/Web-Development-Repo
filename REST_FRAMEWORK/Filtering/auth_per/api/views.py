
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from django.shortcuts import render
from .models import Student
#from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    #filter_backends = [DjangoFilterBackend]
    #filterset_fields  = ['city']

    ## search filter
    filter_backends = [SearchFilter]
    filterset_fields  = ['city','name']

    ## ordering filter
    filter_backends = [OrderingFilter]
    filterset_fields  = ['name']
    



    # IMPORTANT CONCEPT
    #def get_queryset(self):
    #    user = self.request.user
    #    return Student.objects.filter(passby = user)
