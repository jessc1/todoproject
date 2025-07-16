import pytest
from todo.models import Todo, User


@pytest.mark.django_db
def test_creating_todo():
    user = User.objects.create(username="cheng yi", password="1234")
    obj = Todo.objects.create(user=user,title="Watching SuperMan", description="go to theater watch the new superman movie", is_done=False)
    assert user.username == "cheng yi"
    assert user.password == "1234"
    assert obj.title == "Watching SuperMan"
    assert obj.description == "go to theater watch the new superman movie"
    assert obj.is_done == False
    assert Todo.objects.count() == 1






  
    
