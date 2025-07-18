import pytest
from rest_framework.test import APIClient
from rest_framework import status
from todo.models import User

data_user = {
    "username": "test_user",
    "password": "test1234"
}

@pytest.fixture
def user(db) -> User:
    return User.objects.create_user(**data_user)


@pytest.fixture
def client():
    return APIClient()

class TestAuthenticationViewSet:
    endpoint = '/api/auth/'

    def test_login(self, client, user):
        data = {"username": user.username, "password": "test1234"}
        response = client.post(self.endpoint + "login/", data)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['access']        
        assert response.data['user']['username'] == user.username
    
    @pytest.mark.django_db
    def test_register(self, client):
        data = {
            "username": "usertest",
            "password": "test1234"
        }
        response = client.post(self.endpoint + "register/", data)
        assert response.status_code == status.HTTP_201_CREATED
    
    def test_refresh(self, client, user):
        data = {
            "username": user.username,
            "password": "test1234"
        }
        response = client.post(self.endpoint + "login/", data)
        assert response.status_code == status.HTTP_200_OK
        data_refresh = {
            "refresh": response.data['refresh']
        }
        response = client.post(self.endpoint + "refresh/", data_refresh)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['access']

