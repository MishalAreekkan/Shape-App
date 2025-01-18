from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from avatar.models import Avatar


class AvatarViewTest(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email="testuser@example.com",
            password="testpassword123",
            username="TestUser",
        )
        self.avatar_url = "/avatar/avatar/"  

        refresh = RefreshToken.for_user(self.user)
        self.token = str(refresh.access_token)

        Avatar.objects.create(
            user=self.user,
            gender="Male",
            skin_tone="Fair",
            hair_style="Short",
            clothing={},
            accessories={},
        )

    def test_get_avatar(self):
        response = self.client.get(
            self.avatar_url, HTTP_AUTHORIZATION=f"Bearer {self.token}"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertIn("gender", response.data)
        self.assertEqual(response.data["gender"], "Male")
        self.assertIn("skin_tone", response.data)
        self.assertEqual(response.data["skin_tone"], "Fair")

    def test_post_avatar(self):
        avatar_data = {
            "gender": "Female",
            "skin_tone": "Medium",
            "hair_style": "Long",
            "clothing": {
                "top": "Shirt",
                "bottom": "Jeans",
                "shoes": "Sneakers",
            },
            "accessories": {},
        }

        response = self.client.post(
            self.avatar_url,
            avatar_data,
            HTTP_AUTHORIZATION=f"Bearer {self.token}",
            format="json",
        )
        print(response.data, "dfdsfds")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(response.data["gender"], "Female")
        self.assertEqual(response.data["skin_tone"], "Medium")

        avatar = Avatar.objects.get(user=self.user)
        self.assertEqual(avatar.gender, "Female")
        self.assertEqual(avatar.skin_tone, "Medium")

    def test_unauthorized_access(self):
        response = self.client.get(self.avatar_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.post(
            self.avatar_url, {"gender": "Male", "skin_tone": "Fair"}
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
