from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import User, Todo

class UsersSerializer(serializers.ModelSerializer):    
    id = serializers.IntegerField(read_only=True)    

    class Meta:
        model = User
        fields = ['id', 'username']
        read_only_field = ['is_active']

class TodoSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')    
    
    class Meta:
        model = Todo
        fields = ['id','user', 'task', 'is_done', 'created_at', 'updated_at']
        read_only_field = ['created_at']

    def validate_user(self, attr):
        if self.context["request"].user != attr:
            raise ValidationError("cannot create a task for another user")
        return attr   
    
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)



        
