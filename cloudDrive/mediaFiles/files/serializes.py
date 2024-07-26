from rest_framework import serializers 
# serializers convert complex data to json format
from .models import *

class  PostSerializer(serializers.ModelSerializer):
    poster = serializers.ReadOnlyField(source = 'poster.username')
    poster_id = serializers.ReadOnlyField(source = 'poster.id')
    votes = serializers.SerializerMethodField()
    class Meta:
        model  = Post
        fields = ['id','title','url','poster','created_at','poster_id','votes']

    def  get_votes(self,post):
        return Vote.objects.filter(post= post).count()

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['id']

class VoteDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['id']
                        