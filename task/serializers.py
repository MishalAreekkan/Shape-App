from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("id", "task_log", "description", "completed_at")
        read_only_fields = ("completed_at",)
