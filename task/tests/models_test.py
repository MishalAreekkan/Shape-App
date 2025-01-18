from django.test import TestCase
from django.contrib.auth.models import User
from task.models import Task


class TaskModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="password123"
        )

    def test_task_creation(self):
        task = Task.objects.create(
            user=self.user,
            task_log="Test task",
            description="This is a test task",
        )

        self.assertEqual(task.user.username, "testuser")
        self.assertEqual(task.task_log, "Test task")
        self.assertEqual(task.description, "This is a test task")
        self.assertIsNotNone(task.completed_at)  
        self.assertTrue(
            task.completed_at <= task.completed_at
        ) 

    def test_task_ordering(self):
        task1 = Task.objects.create(
            user=self.user,
            task_log="First task",
            description="First task description",
        )
        task2 = Task.objects.create(
            user=self.user,
            task_log="Second task",
            description="Second task description",
        )


        tasks = Task.objects.all()
        self.assertEqual(tasks[0], task2)
        self.assertEqual(tasks[1], task1)

    def test_task_null_description(self):
        task = Task.objects.create(
            user=self.user, task_log="Task without description", description=None
        )

        self.assertIsNone(task.description)
