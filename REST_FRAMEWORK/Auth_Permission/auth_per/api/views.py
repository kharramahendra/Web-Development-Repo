
from .serializers import StudentSerializer
from .models import Student
from rest_framework import viewsets

## ---------- AUTHENTICATION AND PERMISSIONS -----------------------------------+
from rest_framework.authentication import BasicAuthentication,SessionAuthentication              #   |
from rest_framework.permissions import IsAuthenticated,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly,IsAuthenticatedOrReadOnly,AllowAny,IsAdminUser #   |
## DJANGOMODELPERMISSIONs - GIVE PERMISSIONS TO USER AS PER DJANGO USER SYSTEM (authenticataed is complesery)
## DjangoModelPermissionsOrAnonReadOnly - unauthenticated users also have permission of getting data

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
## -----------------------------------------------------------------------------+



## -------------- CUSTOM PERMISSIONS -------------------------------------------+
from .custompermissions import MyPermission
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [MyPermission]
## -----------------------------------------------------------------------------+
