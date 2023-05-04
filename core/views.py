from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from core.models import User, Task
from core.pagination import ProductPagination
from core.serializers import UserSerializer, UserCreateSerializer, TaskSerializer, TaskCreateSerializer


class UserViewSet(viewsets.ModelViewSet):
    """UserViewSet"""
    queryset = User.objects.all()
    pagination_class = ProductPagination

    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        else:
            return UserSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()


class TaskViewSet(viewsets.ModelViewSet):
    """TaskViewSet"""
    queryset = Task.objects.all()
    pagination_class = ProductPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'task_status', 'creator']

    def get_queryset(self):
        """Return an object for the current authenticated user only"""
        if self.request.user.is_staff:
            return self.queryset.all()
        else:
            return self.queryset.filter(creator=self.request.user)

    def get_serializer_class(self):
        if self.action == 'create':
            return TaskCreateSerializer
        else:
            return TaskSerializer


