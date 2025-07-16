from rest_framework import routers
from todo.viewsets import UsersViewSet

router = routers.SimpleRouter()
router.register(r'users', UsersViewSet, basename='users')


urlpatterns = [
    *router.urls,
    ]
