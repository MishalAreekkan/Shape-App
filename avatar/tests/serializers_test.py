from django.test import TestCase
from rest_framework.exceptions import ValidationError
from avatar.models import Avatar
from avatar.serializers import AvatarSerializer
from django.contrib.auth.models import User


class AvatarSerializerTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="password123"
        )

    def test_avatar_serializer_valid_data(self):
        clothing_data = {
            "top": "blue shirt",
            "bottom": "black pants",
            "shoes": "white sneakers",
        }

        avatar_data = {
            "user": self.user.id,
            "gender": "Male",
            "skin_tone": "Fair",
            "hair_style": "Short",
            "clothing": clothing_data,
            "accessories": {"glasses": "round"},
        }

        serializer = AvatarSerializer(data=avatar_data)

        self.assertTrue(serializer.is_valid())

        self.assertEqual(serializer.validated_data["clothing"], clothing_data)

    def test_avatar_serializer_invalid_clothing_data(self):
        clothing_data = {"top": "blue shirt", "bottom": "black pants"}

        avatar_data = {
            "user": self.user.id,
            "gender": "Male",
            "skin_tone": "Fair",
            "hair_style": "Short",
            "clothing": clothing_data,
            "accessories": {"glasses": "round"},
        }

        serializer = AvatarSerializer(data=avatar_data)

        self.assertFalse(serializer.is_valid())

        self.assertIn(
            "Clothing must contain all required fields: top, bottom, shoes",
            str(serializer.errors["clothing"]),
        )

    def test_avatar_serializer_missing_clothing_field(self):
        avatar_data = {
            "user": self.user.id,
            "gender": "Male",
            "skin_tone": "Fair",
            "hair_style": "Short",
            "clothing": {},
            "accessories": {"glasses": "round"},
        }

        serializer = AvatarSerializer(data=avatar_data)

        self.assertFalse(serializer.is_valid())

        self.assertIn(
            "Clothing must contain all required fields: top, bottom, shoes",
            str(serializer.errors["clothing"]),
        )
