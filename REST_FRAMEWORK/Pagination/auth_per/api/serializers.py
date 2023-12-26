from django.db.models import fields
from requests.models import ReadTimeoutError
from rest_framework import serializers, validators
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','name','roll','city']
