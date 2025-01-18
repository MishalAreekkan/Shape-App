from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from task.models import Task
from task.serializers import TaskSerializer

User = get_user_model()


class TaskSerializerTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="example", password="password123")

    def test_task_serializer_valid(self):
        data = {
            "task_log": "Test task",
            "description": "This is a test task",
            "completed_at": None,  
        }

        serializer = TaskSerializer(data=data)

        self.assertTrue(serializer.is_valid())
        task = serializer.save(user=self.user) 

        self.assertEqual(
            task.user, self.user
        )
        self.assertEqual(task.task_log, "Test task")
        self.assertEqual(task.description, "This is a test task")
