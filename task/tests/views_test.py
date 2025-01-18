from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from task.models import Task


class TaskViewTest(APITestCase):
    def setUp(self):
        # Create a user for testing
        self.user = get_user_model().objects.create_user(
            email="testuser@example.com",
            password="testpassword123",
            username="TestUser",
        )
        # Generate JWT token for the user
        refresh = RefreshToken.for_user(self.user)
        self.token = str(refresh.access_token)

        # URL for task endpoint
        self.url = "/task/tasks/"  # Ensure this URL is correct

    def test_get_tasks(self):
        # Test that tasks can be retrieved for the authenticated user
        # Create one task for the user (use 'task_log' instead of 'title')
        Task.objects.create(
            user=self.user,
            task_log="Test Task 1",
            description="Test description",
            completed_at="2025-01-01",
        )

        # Send GET request with the token
        response = self.client.get(self.url, HTTP_AUTHORIZATION=f"Bearer {self.token}")

        # Assert that the status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert that the response contains one task
        self.assertEqual(
            len(response.data["results"]), 1
        )  # Only one task should be returned
        self.assertEqual(response.data["results"][0]["task_log"], "Test Task 1")

    def test_post_task(self):
        # Test that a new task can be created
        task_data = {
            "task_log": "New Task",  # Use 'task_log' instead of 'title'
            "description": "New task description",
            "completed_at": "2025-01-01",
        }

        # Send POST request to create a task
        response = self.client.post(
            self.url,
            task_data,
            HTTP_AUTHORIZATION=f"Bearer {self.token}",
            format="json",
        )

        # Assert that the status code is 201 Created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Assert that the task data is correct
        self.assertEqual(
            response.data["task_log"], "New Task"
        )  # 'task_log' instead of 'title'
        self.assertEqual(response.data["description"], "New task description")

        # Check that the task is actually saved in the database
        task = Task.objects.get(
            user=self.user, task_log="New Task"
        )  # Ensure you're querying the correct task
        self.assertEqual(task.task_log, "New Task")  # 'task_log' instead of 'title'
        self.assertEqual(task.description, "New task description")

    def test_unauthorized_access(self):
        # Test that unauthorized users cannot access the task API

        # Try GET request without authorization
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # Try POST request without authorization
        response = self.client.post(
            self.url, {"task_log": "Unauthorized Task"}
        )  # 'task_log' instead of 'title'
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
