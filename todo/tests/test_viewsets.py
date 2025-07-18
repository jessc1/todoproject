import pytest
from rest_framework import status
from todo.models import Todo
from auth.tests import user, client

@pytest.fixture
def task(db, user):
    return Todo.objects.create(user=user, task="test task", is_done=True)

class TestTodoViewSet:
    endpoint = '/api/tasks/'

    def test_todo_list(self, client, user, task):
        client.force_authenticate(user=user)
        response = client.get(self.endpoint)
        assert response.status_code == status.HTTP_200_OK
        assert response.data["count"] == 1
    
    def test_retrieve(self, client, user, task):
        client.force_authenticate(user=user)
        response = client.get(self.endpoint + str(task.id) + "/")
        assert response.status_code == status.HTTP_200_OK
        assert response.data['id'] == task.id
        assert response.data['task'] == task.task
        assert response.data['user'] == user.username
    
    def test_create(self, client, user):
        client.force_authenticate(user=user)
        data = {"user": "test_user", "task": "test task", "is_done": False}
        response = client.post(self.endpoint, data)
        assert response.status_code == status.HTTP_201_CREATED
    
    def test_update(self, client, user, task):
        client.force_authenticate(user=user)
        data = {"user": "test_user", "task": "test task", "is_done": False}
        response = client.put(self.endpoint + str(task.id) + "/", data)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['task'] == data['task']
    
    def test_delete(self, client, user, task):
        client.force_authenticate(user=user)
        response = client.delete(self.endpoint + str(task.id) + "/")
        assert response.status_code == status.HTTP_204_NO_CONTENT

        



        
