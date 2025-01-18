from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Avatar(models.Model):
    GENDER_CHOICES = [("Male", "Male"), ("Female", "Female"), ("Other", "Other")]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    skin_tone = models.CharField(max_length=50)
    hair_style = models.CharField(max_length=50)
    clothing = models.JSONField(null=True, blank=True)
    accessories = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_at"]
