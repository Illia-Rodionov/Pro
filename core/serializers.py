from rest_framework import serializers

from core.models import User, Task


class UserCreateSerializer(serializers.ModelSerializer):
    """UserCreateSerializer"""
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


class UserSerializer(serializers.ModelSerializer):
    """Read Update Delete UserSerializer"""
    created_at = serializers.CharField(read_only=True)
    updated_at = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'created_at', 'updated_at')


class TaskCreateSerializer(serializers.ModelSerializer):
    creator = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    creator = serializers.CharField(read_only=True)

    class Meta:
        model = Task
        fields = ('name', 'description', 'task_status', 'creator')

    def create(self, validated_data):
        """creator == user.request"""
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)


class TaskSerializer(serializers.ModelSerializer):
    """TaskSerializer"""
    creator = serializers.SlugRelatedField(slug_field='email', queryset=User.objects.all())
    created_at = serializers.CharField(read_only=True)
    updated_at = serializers.CharField(read_only=True)

    class Meta:
        model = Task
        fields = ('name', 'description', 'creator', 'task_status', 'created_at', 'updated_at')

