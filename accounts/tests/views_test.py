from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User


class UserViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.user_data = {"username": "testuser", "password": "testpassword"}
        self.profile_url = reverse("profile")
        self.register_url = reverse("register")
        self.login_url = reverse("login")

    def test_register_user(self):
        register_data = {
            "username": "newuser",
            "password": "newpassword",
            "confirm_password": "newpassword",
            "email": "newuser@example.com",
        }
        response = self.client.post(self.register_url, register_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("message", response.data)

    def test_login_user(self):
        response = self.client.post(self.login_url, self.user_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)

    def test_profile_get(self):
        token = self._get_token_for_user(self.user)
        response = self.client.get(
            self.profile_url, HTTP_AUTHORIZATION=f"Bearer {token}"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["username"], self.user.username)

    def test_profile_put(self):
        token = self._get_token_for_user(self.user)
        update_data = {"username": "updateduser", "email": "updateduser@example.com"}
        response = self.client.put(
            self.profile_url,
            update_data,
            content_type="application/json",
            HTTP_AUTHORIZATION=f"Bearer {token}",
            format="json",
        )
        print(response.data, "sdfdsgssgsgs")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, "updateduser")

    def _get_token_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)
