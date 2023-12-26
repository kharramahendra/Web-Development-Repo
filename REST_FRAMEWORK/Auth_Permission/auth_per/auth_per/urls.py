
from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter

## creating router object
router = DefaultRouter()

## Register Student view set
router.register('studentapi',views.StudentViewSet,basename = 'student')



urlpatterns = [
    path('admin/', admin.site.urls),

## ---------- FOR GENERICS AND MODEL MIXINS ---------------------------
    #path('studentapi/',views.StudentList.as_view()),
    #path('studentapi/',views.StudentCreate.as_view()),
    #path('studentapi/<int:pk>',views.StudentRetrieve.as_view()),
    #path('studentapi/<int:pk>',views.StudentUpdate.as_view()),
    #path('studentapi/<int:pk>',views.StudentDestroy.as_view()),

    #path('studentapi/',views.LCStudentAPI.as_view()),
    #path('studentapi/<int:pk>',views.RUDStudentAPI.as_view()),


## ---------------- FOR LISTAPIView ------------------------------------
    #path('studentapi/',views.StudentList.as_view()),

## --------------- FOR ViewSet -----------------------------------------
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework'))

]
