from rest_framework import serializers
from todo.serializers import UsersSerializer
from todo.models import User

class RegisterSerializer(UsersSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
