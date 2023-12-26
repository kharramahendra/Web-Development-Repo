from rest_framework.utils import serializer_helpers
from .models import Singer, Song
from rest_framework import serializers

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id','title','singer','duration']
    
class SingerSerializer(serializers.ModelSerializer):
    #song = serializers.StringRelatedField(many=True,read_only=True)
    #song = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    song = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='song-detail')
    class Meta:
        model = Singer
        fields  = ['id','name','gender','song']