from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets

# short way to  create a view with all functions
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# short way to create list() and retrieve()
class StudentModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer