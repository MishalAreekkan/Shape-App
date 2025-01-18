from django.test import TestCase
from django.contrib.auth.models import User
from avatar.models import Avatar


class AvatarModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="password123"
        )

    def test_avatar_creation(self):
        avatar = Avatar.objects.create(
            user=self.user,
            gender="Male",
            skin_tone="Fair",
            hair_style="Short",
            clothing={"shirt": "blue", "pants": "black"},
            accessories={"glasses": "round"},
        )

        self.assertEqual(avatar.user.username, "testuser")
        self.assertEqual(avatar.gender, "Male")
        self.assertEqual(avatar.skin_tone, "Fair")
        self.assertEqual(avatar.hair_style, "Short")
        self.assertEqual(avatar.clothing, {"shirt": "blue", "pants": "black"})
        self.assertEqual(avatar.accessories, {"glasses": "round"})
        self.assertIsNotNone(avatar.created_at)
        self.assertIsNotNone(avatar.updated_at)

    def test_avatar_ordering(self):
        avatar1 = Avatar.objects.create(
            user=self.user,
            gender="Female",
            skin_tone="Dark",
            hair_style="Curly",
            clothing={"dress": "red"},
            accessories={"earrings": "gold"},
        )
        avatar2 = Avatar.objects.create(
            user=self.user,
            gender="Other",
            skin_tone="Olive",
            hair_style="Long",
            clothing={"shirt": "green"},
            accessories={"hat": "black"},
        )

        avatars = Avatar.objects.all()
        self.assertEqual(avatars[0], avatar2)
        self.assertEqual(avatars[1], avatar1)
