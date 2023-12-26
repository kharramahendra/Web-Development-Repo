
from .serializers import StudentSerializer
from .models import Student
from rest_framework import viewsets

## ---------- AUTHENTICATION AND PERMISSIONS -----------------------------------+
from rest_framework.authentication import BasicAuthentication,SessionAuthentication              #   |
from rest_framework.permissions import IsAuthenticated,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly,IsAuthenticatedOrReadOnly,AllowAny,IsAdminUser #   |
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle,ScopedRateThrottle
from api.throttling import JackRateThrottle

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    #throttle_classes = []
    throttle_classes = [AnonRateThrottle,JackRateThrottle]


## WE CAN USE SCOPERATETHROTTLE FOR DIFFERENT DIFFERENT CLASSES AND CAN SET THE SCOPE VALUE

##  throttle_classes = [ScopeRateThrottle]
##  throttle_scope = 'get_ka_scope'