from django.db.models import fields
from rest_framework import serializers
from .models import Student





# 1.Validators
def start_with_r(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError("the name must start with r")

## this type of serializer is reguler serializer
class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100,validators = [start_with_r])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    def create(self,validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self, instance,validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.roll = validated_data.get('roll',instance.roll)
        instance.city = validated_data.get('city',instance.city)
        instance.save()
        return instance
    
    ## validation writing
    ## 2.field level validation
    def validate_roll(self,value):
        if value >= 2000:
            raise serializers.ValidationError("roll number is too big")
        return value
    
    ## 3.object level validation
    def validate(self,data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'kaluram' and ct.lower() != 'nagaur':
            raise serializers.ValidationError('city must be nagaur')
        return data
