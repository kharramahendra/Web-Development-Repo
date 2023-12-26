
from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

router = DefaultRouter()
router.register('studentapi',views.StudentViewSet,basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('gettoken/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('refreshtoken/',TokenRefreshView.as_view(),name='token_refresh'),
    path('verifytoken/',TokenVerifyView.as_view(),name='token_verify')
]

## generating token
##  http POST http://127.0.0.1:8000/gettoken/ username="pawan" password="kaluram1236"

## verifying token
##  http POST http://127.0.0.1:8000/verifytoken/ token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMyODExOTQ1LCJqdGkiOiIyMGU5YTZjZmFmYzA0YWMwOGU2NTE2MDVjZjkyZjNhMyIsInVzZXJfaWQiOjR9.b3qi6yR8wVIxE7mucnUZMiAi6gymTdJNhISIHk2mUzI"

## refreshing token
## 