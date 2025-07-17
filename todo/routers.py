from rest_framework import routers
from todo.viewsets import UsersViewSet, TodoViewSet

router = routers.SimpleRouter()
router.register(r'users', UsersViewSet, basename='users')
router.register(r'tasks', TodoViewSet, basename='tasks')
urlpatterns = [
    *router.urls,
    ]
