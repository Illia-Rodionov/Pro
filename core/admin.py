from django.contrib import admin

from core.models import User, Task


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass
