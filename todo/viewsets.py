from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import filters
from todo.serializers import UsersSerializer, TodoSerializer
from todo.models import User, Todo

class UsersViewSet(viewsets.ModelViewSet):
    http_method_names = ('patch', 'get')    
    permission_classes = [IsAuthenticated]
    serializer_class = UsersSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()
        return User.objects.exclude(is_superuser=True)

    def get_object_by_id(self):
        obj = User.objects.get(self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj
   
class TodoViewSet(viewsets.ModelViewSet):
    http_method_names = ('post', 'get', 'put', 'delete')    
    permission_classes = [IsAuthenticated]
    serializer_class = TodoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['task']

    def get_queryset(self):
        return Todo.objects.all()
    
    def get_object_by_id(self):
        obj = Todo.objects.get(self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        
        return Response(serializer.data)
    
