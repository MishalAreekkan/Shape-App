from django.test import TestCase
from django.contrib.auth.models import User
from accounts.serializers import (
    UserRegistrationSerializer,
    UserLoginSerializer,
    UserProfileSerializer,
)


class UserRegistrationSerializerTest(TestCase):
    def test_valid_registration(self):
        data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "Password123!",
            "confirm_password": "Password123!",
        }
        serializer = UserRegistrationSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()
        self.assertEqual(user.username, data["username"])
        self.assertEqual(user.email, data["email"])
        self.assertTrue(user.check_password(data["password"]))

    def test_password_mismatch(self):
        data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "Password123!",
            "confirm_password": "DifferentPassword123!",
        }
        serializer = UserRegistrationSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("password", serializer.errors)
        self.assertEqual(serializer.errors["password"][0], "Passwords do not match.")


class UserLoginSerializerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", email="testuser@example.com", password="Password123!"
        )

    def test_generate_token(self):
        serializer = UserLoginSerializer()
        token = serializer.get_token(self.user)
        self.assertIn("username", token)
        self.assertIn("email", token)
        self.assertEqual(token["username"], self.user.username)
        self.assertEqual(token["email"], self.user.email)


class UserProfileSerializerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", email="testuser@example.com", password="Password123!"
        )

    def test_user_profile_data(self):
        serializer = UserProfileSerializer(instance=self.user)
        data = serializer.data
        self.assertEqual(data["username"], self.user.username)
        self.assertEqual(data["email"], self.user.email)
        self.assertIn("id", data)
