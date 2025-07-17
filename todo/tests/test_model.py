import pytest
from todo.models import User, Todo


@pytest.mark.django_db
def test_creating_todo():
    user = User.objects.create(username="chengyi", password="1234")
    obj = Todo.objects.create(user=user,task="Watching SuperMan", is_done=False)
    assert user.username == "chengyi"
    assert user.password == "1234"
    assert obj.task == "Watching SuperMan"
    assert obj.is_done == False
    assert Todo.objects.count() == 1
