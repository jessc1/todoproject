import pytest
from todo.models import Todo

@pytest.mark.django_db
def test_creating_todo():
    obj = Todo.objects.create(title="Watching SuperMan", description="go to theater watch the new superman movie", is_done=False,)
    assert obj.title == "Watching SuperMan"
    assert obj.description == "go to theater watch the new superman movie"
    assert obj.is_done == False
    assert Todo.objects.count() == 1





  
    
