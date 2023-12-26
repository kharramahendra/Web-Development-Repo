from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('singer',views.SingerViewSet,basename='singer')
router.register('song',views.SongViewSet,basename='song')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework')),
]
