from django.urls import path
from .views import AvatarView

urlpatterns = [
    path("avatar/", AvatarView.as_view(), name="avatar"),
]
