## concrete view 
from rest_framework import serializers
from .models import Student
from .serializers import StudentSerializer


## ----------- FOR DEFFERENT DIFFERENT METHODS --------------------
from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView
## ----------- FOR COMBINATION ------------------------------------
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView 
## ------------------------------------------------------------------------------------------------------------



class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentCreate(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieve(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentUpdate(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDestroy(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer