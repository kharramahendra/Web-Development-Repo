from django.db.models import fields
from requests.models import ReadTimeoutError
from rest_framework import serializers, validators
from .models import Student



# 1.Validators
def start_with_r(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError("the name must start with r")

## model serializer
class StudentSerializer(serializers.ModelSerializer):
   
    #1.read only field //THIS IS NOT WORKING
       #name = serializers.CharField(read_only = True)

    #name = serializers.CharField(validators = [start_with_r])
    class Meta:
        model = Student
        fields = ['id','name','roll','city']

        #2.way
        #read_only_fields = ['name','roll'] 
        #if we do this then user can not cahnge the name of any object

        #3.way
        #extra_kwargs = {'name':{'read_only':True}}

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


    
    # in modelserializer we don't have to create update or create function

