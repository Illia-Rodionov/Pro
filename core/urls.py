from django.urls import include, path

from core.views import UserViewSet, TaskViewSet
from rest_framework import routers


app_name = "core"

router = routers.SimpleRouter()


router.register(r"task", TaskViewSet, basename='task')
router.register(r"user", UserViewSet, basename='user')

urlpatterns = [
    path("", include(router.urls)),
]