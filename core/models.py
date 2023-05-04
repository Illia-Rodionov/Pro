from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from core.managers import UserManager


class User(AbstractUser, PermissionsMixin):
    """User model"""
    username = models.CharField(max_length=100, null=True, blank=True, unique=True)
    email = models.EmailField(max_length=100, db_index=True, unique=True, null=False, blank=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def get_username(self):
        return self.email


class Task(models.Model):
    UNRESOLVED_STATUS = 1
    IN_PROGRESS_STATUS = 2
    RESOLVED_STATUS = 3

    TASK_STATUS_CHOICES = (
        (UNRESOLVED_STATUS, "UNRESOLVED"),
        (IN_PROGRESS_STATUS, "IN_PROGRESS"),
        (RESOLVED_STATUS, "RESOLVED"),
    )

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    creator = models.ForeignKey('User', on_delete=models.CASCADE, related_name='task_creator')
    task_status = models.PositiveSmallIntegerField(default=UNRESOLVED_STATUS, choices=TASK_STATUS_CHOICES)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

