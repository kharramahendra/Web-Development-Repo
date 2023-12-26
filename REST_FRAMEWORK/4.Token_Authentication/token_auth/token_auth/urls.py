# for custom token authentication
from api.auth import CustomAuthToken

from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter
#for token authentication
from rest_framework.authtoken.views import obtain_auth_token



router = DefaultRouter()
router.register('studentapi',views.StudentViewSet,basename = 'student')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),

    #for session authentication
    #path('auth/',include('rest_framework.urls',namespace='rest_framework')),

    # for token authentication
    #path('gettoken',obtain_auth_token)

    #for custom authentication
    #path('gettoken/',CustomAuthToken.as_view())

]

##  http POST http://127.0.0.1:8000/gettoken/ username="mukesh" password="kaluramkharra"