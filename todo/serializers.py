from rest_framework import serializers
from .models import User, Todo

class UsersSerializer(serializers.ModelSerializer):    
    id = serializers.IntegerField(read_only=True)    

    class Meta:
        model = User
        fields = ['id', 'username']
        read_only_field = ['is_active']

        
