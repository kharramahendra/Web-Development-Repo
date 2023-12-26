
from .serializers import StudentSerializer
from .models import Student
from rest_framework import viewsets

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly,IsAuthenticatedOrReadOnly,AllowAny,IsAdminUser #   |

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


# GET REQUEST
# http POST http://127.0.0.1:8000/studentapi/ 'Authorization:Token 97319a4c18cc816efec56f8960da99c386b80a8d
# POST REQUEST
# http -f POST http://127.0.0.1:8000/studentapi/ name=pawan roll=103 city=Merta 'Authorization:Token 97319a4c18cc816efec56f8960da99c386b80a8d' 
# PUT 
# http PUT http://127.0.0.1:8000/studentapi/ name=pawan roll=103 city=NAGAUR 'Authorization:Token 97319a4c18cc816efec56f8960da99c386b80a8d'