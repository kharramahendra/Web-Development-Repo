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








# from scratch api === full customization 
# apiview - full cusomization with power of DRF{{{PERFECT FOR HEAVY USE}}}

# generic api view -- low customisation (short code)
# concrete api view - almost similar customization and code with generic api view 
# viewset - 2-3 line of code and get full functionality